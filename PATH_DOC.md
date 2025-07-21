# Entry-point scripts

The python packages with a command all have a corresponding entry-point script that runs a specific function. For instance, the `amon` command executes its entry-point script, which itself executes the package's main function.

Therefore, the location of this script is necessary if we want to add it to `PATH`, or run it directly. 

## Where is the entry-point script's directory?

> Note: For virtual environments, the script should be added to `PATH` automatically. If not, please consult the virtual environment's documentation.

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

The script's directory's path is what needs to be added to `PATH`.

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

