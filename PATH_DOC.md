# Adding `amon` to `PATH`

If the `python` command is not found, install python and/or add it to `PATH` (see https://realpython.com/add-python-to-path/)

## What to add to `PATH`?

The entry-point scripts, or commands, of pip-installed packages reside in a specific directory. It is this directory that needs to be added to `PATH`.

### System-wide install

- Entry-point scripts go to:
  - macOS/Linux: `/usr/local/bin/`
  - Windows: `C:\Python3x\Scripts\`
- Check with:

```bash
python -c "import sysconfig; print(sysconfig.get_path('scripts'))"
```

### User-level Install (with pip install --user amon-bb or with restricted access rights)

- Entry-point scripts go to:
  - macOS: `~/Library/Python/3.x/bin/`
  - Linux: `~/.local/bin/`
  - Windows: `%APPDATA%\Python\Python3x\Scripts\`
- Check with:

```bash
python -m site --user-base
```

## Adding to `PATH`

### MacOS and Linux

If using `bash`:  
```bash 
echo 'export PATH="path/to/amon/directory:$PATH"' >> ~/.bashrc 
source ~/.bashrc 
``` 
If using `zsh`: 
 
```bash 
echo 'export PATH="path/to/amon/directory:$PATH"' >> ~/.zshrc 
source ~/.zshrc 
``` 

> Note: To change the current shell session's `PATH` only: `export PATH="path/to/amon/directory:$PATH"`

### Windows

Consult https://www.eukhost.com/kb/how-to-add-to-the-path-on-windows-10-and-windows-11/

