
# For more info on the setup, check out our docs https://alttester.com/docs/sdk/latest/pages/get-started.html#write-and-execute-first-test-for-your-app  
import unittest
from alttester import By, AltKeyCode, AltDriver

class MyTests(unittest.TestCase):

  start_button_path = "/Canvas/StartButton"
  start_button_path1 = "/UICamera/Loadout/StartButton"
  pause_button_path = "/UICamera/Game/WholeUI/pauseButton"
  resume_path = "/UICamera/Game/PauseMenu/Resume"

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
    start_button1 = self.alt_driver.wait_for_object(By.PATH, self.start_button_path1, timeout=20)
    start_button1.click()
    pause_button = self.alt_driver.wait_for_object(By.PATH, self.pause_button_path, timeout=20)
    pause_button.click()
    resume = self.alt_driver.wait_for_object(By.PATH, self.resume_path, timeout=20)
    resume.click()
    self.alt_driver.load_scene("Start", True)
