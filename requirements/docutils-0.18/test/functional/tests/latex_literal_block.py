# Source and destination file names.
test_source = "latex_literal_block.txt"
test_destination = "latex_literal_block.tex"

# Keyword parameters passed to publish_file.
reader_name = "standalone"
parser_name = "rst"
writer_name = "latex"

# Extra setting we need
settings_overrides['syntax_highlight'] = 'none'
settings_overrides['stylesheet'] = 'docutils'
