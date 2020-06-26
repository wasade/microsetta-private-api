import unittest

from microsetta_private_api.repo.kit_repo import KitRepo
from microsetta_private_api.repo.transaction import Transaction


class KitRepoTests(unittest.TestCase):
    def setUp(self):
        self.invalid_kit_id_uuid = '00000000-0000-0000-0000-000000000000'
        self.valid_kit_id_uuid = 'd8592c74-9695-2135-e040-8a80115d6401'
        self.valid_kit_id = 'DokBF'
        self.valid_kit_barcodes = set(['000004213', '000004214', '000004215',
                                       '000004216', '000004217', '000004218',
                                       '000004219'])
        self.valid_kit_id_with_unassigned = 'bg_mqsgt'
        self.invalid_kit_id = 'some kit id that does not exist'

    def test_get_kit_all_samples_by_kit_id(self):
        with Transaction() as t:
            kit_repo = KitRepo(t)
            kit = kit_repo.get_kit_all_samples_by_kit_id(
                    self.valid_kit_id_uuid)
            obs = {k['sample_barcode'] for k in kit.to_api()}
            self.assertEqual(obs, self.valid_kit_barcodes)

            kit = kit_repo.get_kit_all_samples_by_kit_id(
                    self.invalid_kit_id_uuid)
            self.assertEqual(kit, None)

    def test_get_kit_all_samples(self):
        with Transaction() as t:
            kit_repo = KitRepo(t)
            kit = kit_repo.get_kit_all_samples(self.valid_kit_id)
            obs = {k['sample_barcode'] for k in kit.to_api()}
            self.assertEqual(obs, self.valid_kit_barcodes)
            obs = kit_repo.get_kit_all_samples(self.invalid_kit_id)
            self.assertEqual(obs, None)

    def test_get_kit_unused_samples(self):
        exp = {'000033075', '000033076'}
        with Transaction() as t:
            kit_repo = KitRepo(t)
            kit = kit_repo.get_kit_unused_samples(
                    self.valid_kit_id_with_unassigned)
            obs = {k['sample_barcode'] for k in kit.to_api()}
            self.assertEqual(obs, exp)

            # all samples are claimed
            kit = kit_repo.get_kit_unused_samples(
                    self.valid_kit_id)
            self.assertEqual(kit, None)

    def test_get_kit_exists(self):
        with Transaction() as t:
            kit_repo = KitRepo(t)
            self.assertTrue(kit_repo.get_kit_exists(self.valid_kit_id))
            self.assertFalse(kit_repo.get_kit_exists(self.invalid_kit_id))


if __name__ == '__main__':
    unittest.main()
