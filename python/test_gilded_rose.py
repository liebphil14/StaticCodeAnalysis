# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_all_items_after_one_day(self):
        items = [
            Item("+5 Dexterity Vest", 10, 20),
            Item("Aged Brie", 2, 0),
            Item("Elixir of the Mongoose", 5, 7),
            Item("Sulfuras, Hand of Ragnaros", 0, 80),
            Item("Backstage passes to a TAFKAL80ETC concert", 15, 20),
            Item("Conjured Mana Cake", 3, 6)
        ]

        GildedRose(items).update_quality()

        # +5 Dexterity Vest
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(19, items[0].quality)

        # Aged Brie
        self.assertEqual(1, items[1].sell_in)
        self.assertEqual(1, items[1].quality)

        # Elixir of the Mongoose
        self.assertEqual(4, items[2].sell_in)
        self.assertEqual(6, items[2].quality)

        # Sulfuras
        self.assertEqual(0, items[3].sell_in)
        self.assertEqual(80, items[3].quality)

        # Backstage Pass (>10 Tage)
        self.assertEqual(14, items[4].sell_in)
        self.assertEqual(21, items[4].quality)

        # Conjured
        self.assertEqual(2, items[5].sell_in)
        self.assertEqual(4, items[5].quality)
if __name__ == '__main__':
    unittest.main()
