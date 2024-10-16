from gftools.builder.operations.fontc import FontcOperationBase


class FontcBuildTTF(FontcOperationBase):
    description = "Build an OTF from a source file (with fontc)"
    # the '--cff-outlines' flag does not exit in fontc, so this will
    # error, which we want
    rule = "fontc -o $out $in $args --cff-outlines"
