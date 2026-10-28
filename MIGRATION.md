# Migrating from contrastcolors to awesomefigures

The PyPI distribution and Python import package are now **awesomefigures**.
The recommended alias is `af`:

```python
import awesomefigures as af
af.set_style('elegante')
```

To migrate a previously installed editable development environment:

```bash
python -m pip uninstall -y contrastcolors
python -m pip install -e .
```

The previous import name `contrastcolors` is no longer installed by this repository. Previously generated notebook outputs and published demonstration PDFs may still contain the old branding until rebuilt. The canonical GitHub repository is now `awesomefigures/awesomefigures`.
Some older documentation links may still use the legacy Pages host until
its deployment is migrated. The package rename itself does not publish to PyPI.
