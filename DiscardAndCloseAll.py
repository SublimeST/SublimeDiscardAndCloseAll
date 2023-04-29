import sublime
import sublime_plugin

# Shamelessly ripped of from: 
# https://forum.sublimetext.com/t/closing-literally-around-1300-files-add-the-function-to-close-all-files-without-saving/39880/3
class DiscardAndCloseAll(sublime_plugin.WindowCommand):
    def run(self):
        window = self.window

        for v in window.views():
            if v.is_dirty():
                v.set_scratch(True)

        window.run_command("close")
