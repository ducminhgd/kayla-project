from utils.dictionary import sort_by_key
from utils.number import bin_to_hex


class ISO8583(object):
    _mti = None
    _fields = {}

    def set_mti(self, mti):
        self._mti = mti

    def get_mti(self):
        return self._mti

    def set_bit(self, bit, value):
        self._fields[bit] = value

    def get_bitmap(self):
        max_bit = max(self._fields.keys())
        num_bitmap = ((max_bit - 1) / 64) + 1
        bitmaps = ['0' * 64] * num_bitmap
        for bit in self._fields.keys():
            bit_sector = (bit - 1) / 64
            position = (bit - 1) % 64
            bitmaps[bit_sector] = bitmaps[bit_sector][:position] + '1' + bitmaps[bit_sector][position + 1:]
        for i in range(0, num_bitmap):
            bitmaps[i] = bin_to_hex(bitmaps[i], 16)
        return (''.join(bitmaps)).upper()

    def assemble_fields(self):
        sorted_fields = sort_by_key(self._fields)
        string_fields = ''
        for k, v in sorted_fields.items():
            string_fields = '{}{}'.format(string_fields, v)
        return string_fields

    def get_message(self):
        return '{}{}{}'.format(self._mti, self.get_bitmap(), self.assemble_fields())
