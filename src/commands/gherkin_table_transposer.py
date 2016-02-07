import sublime
import sublime_plugin

from src.gherkin.view_formatter import ViewFormatter


class TransposeGherkinTableCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        ViewFormatter(sublime, self.view).format_view(edit)
