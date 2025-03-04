
# For more info on the setup, check out our docs https://alttester.com/docs/sdk/latest/pages/get-started.html#write-and-execute-first-test-for-your-app  
import unittest
from alttester import By, AltKeyCode, AltDriver

class MyTests(unittest.TestCase):

  start_button_path = "/Canvas/StartButton"
  mission_button_path = "/UICamera/Loadout/MissionButton"
  close_button_path = "/UICamera/Loadout/MissionPopup/MissionBackground/CloseButton"

  @classmethod
  def setUp(self):
    self.alt_driver = AltDriver(host="127.0.0.1", port=13000, app_name="__default__")

  # You might want to load the scene here
  #   self.alt_driver.load_scene("Start", True)

  @classmethod
  def tearDown(self):
    self.alt_driver.stop()

  def test(self):
    self.alt_driver.load_scene("Start", True)
    start_button = self.alt_driver.wait_for_object(By.PATH, self.start_button_path, timeout=20)
    start_button.click()
    mission_button = self.alt_driver.wait_for_object(By.PATH, self.mission_button_path, timeout=20)
    mission_button.click()
    close_button = self.alt_driver.wait_for_object(By.PATH, self.close_button_path, timeout=20)
    close_button.click()
    self.alt_driver.load_scene("Start", True)
