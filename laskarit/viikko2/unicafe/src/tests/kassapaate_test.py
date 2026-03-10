import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_kassapaate_luotu_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.00)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_edullisen_lounaan_kateisella_osto_toimii(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(240), 0)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
    
    def test_edullisen_lounaan_kateisella_osto_ei_toimi_jos_maksu_ei_riita(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(239), 239)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_maukkaan_lounaan_kateisella_osto_toimii(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(400), 0)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
    
    def test_maukkaan_lounaan_kateisella_osto_ei_toimi_jos_maksu_ei_riita(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(399), 399)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_edullisen_lounaan_kortilla_osto_toimii(self):
        kortti = Maksukortti(240)
        self.assertTrue(self.kassapaate.syo_edullisesti_kortilla(kortti))
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(kortti.saldo_euroina(), 0.0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_edullisen_lounaan_kortilla_osto_ei_toimii_jos_saldo_ei_riita(self):
        kortti = Maksukortti(239)
        self.assertFalse(self.kassapaate.syo_edullisesti_kortilla(kortti))
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(kortti.saldo_euroina(), 2.39)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maukkaan_lounaan_kortilla_osto_toimii(self):
        kortti = Maksukortti(400)
        self.assertTrue(self.kassapaate.syo_maukkaasti_kortilla(kortti))
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(kortti.saldo_euroina(), 0.0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_maukkaan_lounaan_kortilla_osto_ei_toimii_jos_saldo_ei_riita(self):
        kortti = Maksukortti(399)
        self.assertFalse(self.kassapaate.syo_maukkaasti_kortilla(kortti))
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(kortti.saldo_euroina(), 3.99)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortille_rahan_lataaminen_toimii(self):
        kortti = Maksukortti(240)
        self.kassapaate.lataa_rahaa_kortille(kortti, 1000)
        self.assertEqual(kortti.saldo_euroina(), 12.4)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 101000)
    
    def test_kortille_rahan_lataaminen_ei_toimi_jos_summa_on_negatiivinen(self):
        kortti = Maksukortti(240)
        self.kassapaate.lataa_rahaa_kortille(kortti, -1000)
        self.assertEqual(kortti.saldo_euroina(), 2.4)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)