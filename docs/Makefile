# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = python3 -msphinx
SPHINXINTL    = python3 -msphinx_intl
SPHINXPROJ    = FreeGames
SOURCEDIR     = .
BUILDDIR      = _build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile update-po

update-po: pot
	$(SPHINXINTL) update -p "$(BUILDDIR)/gettext" $(0)

pot: gettext
	@cp $(BUILDDIR)/gettext/*.pot locale/

%-translated: LOCALES = $(patsubst locale/%,%,$(wildcard locale/*))
%-translated:
	@for locale in $(LOCALES); do \
	  SPHINXOPTS="-D language=$$locale"; \
	  BUILDDIR="$(BUILDDIR)/$$locale"; \
	  TARGET="$(patsubst %-translated,%,$@)"; \
	  $(SPHINXBUILD) -M "$$TARGET" "$(SOURCEDIR)" "$$BUILDDIR" $$SPHINXOPTS; \
	done

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
