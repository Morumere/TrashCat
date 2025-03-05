
# For more info on the setup, check out our docs https://alttester.com/docs/sdk/latest/pages/get-started.html#write-and-execute-first-test-for-your-app  
import unittest
from alttester import By, AltKeyCode, AltDriver

class MyTests(unittest.TestCase):

  start_button_path = "/Canvas/StartButton"
  store_button_path = "/UICamera/Loadout/StoreButton"
  count_path = "/Canvas/Background/ItemsList/Container/ItemEntry(Clone)/Icon/Count"
  buy_button_path = "/Canvas/Background/ItemsList/Container/ItemEntry(Clone)/NamePriceButtonZone/PriceButtonZone/BuyButton"

  @classmethod
  def setUp(self):
    self.alt_driver = AltDriver(host="127.0.0.1", port=13000, app_name="__default__")

  # You might want to load the scene here
  #   self.alt_driver.load_scene("Main", True)

  @classmethod
  def tearDown(self):
    self.alt_driver.stop()

  def test(self):
    self.alt_driver.load_scene("Start", True)
    start_button = self.alt_driver.wait_for_object(By.PATH, self.start_button_path, timeout=20)
    start_button.click()
    store_button = self.alt_driver.wait_for_object(By.PATH, self.store_button_path, timeout=20)
    self.alt_driver.hold_button(store_button.get_screen_position(), 0.300293)
    count = self.alt_driver.wait_for_object(By.PATH, self.count_path, timeout=20)
    count.wait_for_component_property("UnityEngine.UI.Text", "enabled", "True", "UnityEngine.UI", 1, get_property_as_string=True, max_depth=1)
    buy_button = self.alt_driver.wait_for_object(By.PATH, self.buy_button_path, timeout=20)
    buy_button.click()
    count1 = self.alt_driver.wait_for_object(By.PATH, self.count_path, timeout=20)
    count1.wait_for_component_property("UnityEngine.UI.Text", "enabled", "True", "UnityEngine.UI", 1, get_property_as_string=True, max_depth=1)
