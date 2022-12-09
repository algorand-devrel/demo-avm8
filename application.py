import pyteal as pt
import beaker as bkr


class DemoAVM8(bkr.Application):
    # define the name of the box we'll use box `boxy`
    _box_name = "boxy"
    box_name = pt.Bytes(_box_name)

    # define the size we'll use for our box, 4k (requires 4 box refs to access)
    _box_size = 1024 * 4  #
    box_size = pt.Int(_box_size)

    flipped_bits = pt.BytesNot(pt.BytesZero(pt.Int(64)))

    # @bkr.external
    # def bootstrap(self, ptxn: pt.abi.PaymentTransaction):
    #    pass

    @bkr.external
    def do_box_stuff(self):
        return pt.Seq(
            # Create a new box  with `box_create`
            pt.Assert(pt.BoxCreate(self.box_name, self.box_size)),
            # Check length of box with `box_len`
            # BoxLen is a `MaybeValue` so it needs to be initialized
            len := pt.BoxLen(self.box_name),
            # should return the full size it was created with
            pt.Assert(len.hasValue(), len.value() == self.box_size),
            # read the bytes to the stack with box_get
            # it is also a `MaybeValue`
            contents := pt.BoxGet(self.box_name),
            # Should have a value and no bits set (bitlen looks for first non 0 bit)
            pt.Assert(contents.hasValue(), pt.BitLen(contents.value()) == pt.Int(0)),
            # write some bytes to our box from 0=>length of bytes
            pt.BoxReplace(self.box_name, pt.Int(0), self.flipped_bits),
            # read the bytes we just wrote
            (read_data := pt.ScratchVar()).store(
                pt.BoxExtract(self.box_name, pt.Int(0), pt.Len(self.flipped_bits))
            ),
            # Should be equal to the bytes we wrote
            pt.Assert(read_data.load() == self.flipped_bits),
            # delete the box (returns a 1 if successfully)
            pt.Assert(pt.BoxDelete(self.box_name)),
        )


if __name__ == "__main__":
    DemoAVM8().dump("artifacts")
