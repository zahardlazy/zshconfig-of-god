#!/usr/bin/env python3
import os
import sys
import datetime
import stat
import argparse
import pwd
from rich.console import Console
from rich.table import Table 
from rich import box
from rich.filesize import decimal

console = Console()

# --- THEME COLORS & CONFIG ---
THEME = {
    "border": "bold cyan",
    "header": "bold white on #005f87",
    "size": "bold spring_green1",
    "user": "bold hot_pink",
    "date_day": "bold gold1",
    "date_time": "dim white",
    "symlink": "italic magenta",
    "dir_default": "bold bright_cyan",
    "file": "bold white",
}

# --- 1. SPECIAL FOLDERS (VSCode Material Theme) ---
FOLDER_MAP = {
    'node_modules': ('', '#E53935'),
    '.git':         ('', '#F44D27'),
    '.github':      ('', '#FFFFFF'),
    '.vscode':      ('', '#007ACC'),
    '.idea':        ('', '#000000'),
    'src':          ('', '#4CAF50'),
    'source':       ('', '#4CAF50'),
    'dist':         ('', '#FF9800'),
    'build':        ('', '#FF9800'),
    'out':          ('', '#FF9800'),
    'public':       ('', '#00BCD4'),
    'assets':       ('', '#00BCD4'),
    'static':       ('', '#00BCD4'),
    'resource':     ('', '#00BCD4'),
    'resources':    ('', '#00BCD4'),
    'images':       ('', '#E040FB'),
    'img':          ('', '#E040FB'),
    'icons':        ('', '#E040FB'),
    'components':   ('', '#FF9800'),
    'views':        ('襁', '#FF9800'),
    'layout':       ('充', '#FF9800'),
    'routes':       ('麗', '#FF9800'),
    'router':       ('麗', '#FF9800'),
    'services':     ('ﲀ', '#FF9800'),
    'api':          ('ﲀ', '#FF9800'),
    'utils':        ('', '#FF9800'),
    'tools':        ('', '#FF9800'),
    'helpers':      ('', '#FF9800'),
    'test':         ('ﭧ', '#8BC34A'),
    'tests':        ('ﭧ', '#8BC34A'),
    'spec':         ('ﭧ', '#8BC34A'),
    '__tests__':    ('ﭧ', '#8BC34A'),
    'docs':         ('', '#2196F3'),
    'doc':          ('', '#2196F3'),
    'config':       ('', '#607D8B'),
    'configs':      ('', '#607D8B'),
    'configuration':('', '#607D8B'),
    'include':      ('', '#90A4AE'),
    'includes':     ('', '#90A4AE'),
    'lib':          ('', '#AB47BC'),
    'library':      ('', '#AB47BC'),
    'libs':         ('', '#AB47BC'),
    'bin':          ('', '#F44336'),
    'scripts':      ('', '#F44336'),
    'env':          ('', '#FFB74D'),
    'venv':         ('', '#3776AB'),
    'temp':         ('', '#FFB74D'),
    'tmp':          ('', '#FFB74D'),
    'log':          ('', '#9E9E9E'),
    'logs':         ('', '#9E9E9E'),
    'hooks':        ('ﯓ', '#FF5252'),
    'plugin':       ('', '#8BC34A'),
    'plugins':      ('', '#8BC34A'),
    'middleware':   ('', '#8BC34A'),
    'theme':        ('', '#2196F3'),
    'themes':       ('', '#2196F3'),
}

# --- 2. EXACT FILE NAMES (Priority) ---
EXACT_FILE_MAP = {
    'package.json':       ('', '#CB3837'),
    'package-lock.json':  ('', '#CB3837'),
    'yarn.lock':          ('', '#2188B6'),
    'pnpm-lock.yaml':     ('', '#F69220'),
    'nodemon.json':       ('', '#76D04B'),
    'webpack.config.js':  ('ﰩ', '#8DD6F9'),
    'rollup.config.js':   ('ﰩ', '#EC4A3F'),
    'babel.config.js':    ('ﬥ', '#F9DC3E'),
    'babelrc':            ('ﬥ', '#F9DC3E'),
    '.babelrc':           ('ﬥ', '#F9DC3E'),
    'tsconfig.json':      ('', '#3178C6'),
    'jsconfig.json':      ('', '#F1E05A'),
    
    'requirements.txt':   ('', '#3776AB'),
    'pipfile':            ('', '#3776AB'),
    'setup.py':           ('', '#3776AB'),
    'manage.py':          ('', '#3776AB'),
    
    'composer.json':      ('', '#8892BE'),
    'composer.lock':      ('', '#8892BE'),
    'artisan':            ('ﳒ', '#FF5722'),
    
    'cargo.toml':         ('', '#DEA584'),
    'cargo.lock':         ('', '#DEA584'),
    
    'dockerfile':         ('', '#2496ED'),
    'docker-compose.yml': ('', '#2496ED'),
    'docker-compose.yaml':('', '#2496ED'),
    
    '.gitignore':         ('', '#F44D27'),
    '.gitattributes':     ('', '#F44D27'),
    '.gitmodules':        ('', '#F44D27'),
    
    '.env':               ('', '#FFB74D'),
    '.env.example':       ('', '#FFB74D'),
    '.env.local':         ('', '#FFB74D'),
    'makefile':           ('', '#6D8086'),
    'jenkinsfile':        ('', '#D24939'),
    'procfile':           ('', '#7C4DFF'),
    'readme.md':          ('', '#42A5F5'),
    'changelog.md':       ('', '#42A5F5'),
    'license':            ('', '#FFEB3B'),
    'license.txt':        ('', '#FFEB3B'),
    'license.md':         ('', '#FFEB3B'),
    'authors':            ('', '#FFEB3B'),
    'contributors':       ('', '#FFEB3B'),
    '.editorconfig':      ('', '#FFF176'),
    '.eslintrc':          ('', '#4B32C3'),
    '.eslintrc.js':       ('', '#4B32C3'),
    '.eslintrc.json':     ('', '#4B32C3'),
    '.prettierrc':        ('', '#F8BBD0'),
    'favicon.ico':        ('', '#FFC107'),
    'robots.txt':         ('ﮧ', '#8BC34A'),
}

# --- 3. EXTENSION MAPPING ---
EXT_MAP = {
    '.html':    ('', '#E34C26'), '.htm': ('', '#E34C26'),
    '.css':     ('', '#1572B6'),
    '.scss':    ('', '#CC6699'), '.sass':('', '#CC6699'),
    '.less':    ('', '#1D365D'), '.styl':('', '#8DC149'),
    '.js':      ('', '#F1E05A'), '.mjs': ('', '#F1E05A'), '.cjs': ('', '#F1E05A'),
    '.ts':      ('', '#3178C6'), '.mts': ('', '#3178C6'), '.cts': ('', '#3178C6'),
    '.d.ts':    ('', '#3178C6'),
    '.jsx':     ('', '#61DAFB'), '.tsx': ('', '#61DAFB'),
    '.vue':     ('﵂', '#41B883'),
    '.svelte':  ('', '#FF3E00'),
    '.ang':     ('', '#DD0031'),
    
    '.py':      ('', '#3776AB'), '.pyc': ('', '#81B2D9'), '.pyd': ('', '#81B2D9'),
    '.java':    ('', '#B07219'), '.class':('', '#B07219'), '.jar': ('', '#B07219'),
    '.c':       ('', '#555555'), '.h':   ('', '#A8B9CC'),
    '.cpp':     ('', '#00599C'), '.hpp': ('', '#A8B9CC'), '.cc':  ('', '#00599C'),
    '.cs':      ('', '#178600'),
    '.go':      ('', '#00ADD8'),
    '.rs':      ('', '#DEA584'), '.rlib':('', '#DEA584'),
    '.php':     ('', '#4F5D95'),
    '.rb':      ('', '#701516'), '.erb': ('', '#701516'),
    '.lua':     ('', '#000080'),
    '.pl':      ('', '#0298C3'), '.pm':  ('', '#0298C3'),
    '.swift':   ('', '#FFAC45'),
    '.kt':      ('', '#F18E33'), '.kts': ('', '#F18E33'),
    '.dart':    ('', '#01579B'),
    '.r':       ('ﳒ', '#276DC3'),
    '.scala':   ('', '#DC322F'),
    '.f':       ('ﳒ', '#734F96'),
    '.clj':     ('', '#5881D8'),
    '.ex':      ('', '#6E4A7E'),
    
    '.json':    ('', '#FBC02D'), '.jsonc':('', '#FBC02D'),
    '.xml':     ('謹', '#FF9800'),
    '.yaml':    ('', '#AA2EEB'), '.yml': ('', '#AA2EEB'),
    '.toml':    ('', '#9C4221'),
    '.ini':     ('', '#6D8086'), '.conf':('', '#6D8086'), '.cfg':('', '#6D8086'),
    '.sql':     ('', '#DAD8D8'),
    '.db':      ('', '#DAD8D8'), '.sqlite':('', '#DAD8D8'),
    '.csv':     ('', '#8BC34A'),
    '.log':     ('', '#FFFFFF'),
    
    '.sh':      ('', '#89E051'),
    '.bash':    ('', '#89E051'),
    '.zsh':     ('', '#89E051'),
    '.fish':    ('', '#89E051'),
    '.bat':     ('', '#C1F12E'),
    '.cmd':     ('', '#C1F12E'),
    '.ps1':     ('', '#42B3F4'),
    '.exe':     ('', '#00A4EF'),
    '.msi':     ('', '#00A4EF'),
    '.bin':     ('', '#FF5252'),
    '.elf':     ('', '#FF5252'),
    '.dll':     ('', '#90A4AE'), '.so':  ('', '#90A4AE'),
    
    '.pcap':    ('', '#26A69A'), '.pcapng':('', '#26A69A'),
    '.pem':     ('', '#E91E63'), '.key':   ('', '#E91E63'),
    '.pub':     ('', '#E91E63'),
    '.crt':     ('﫮', '#E91E63'), '.cer':   ('﫮', '#E91E63'),
    '.apk':     ('', '#3DDC84'),
    '.nse':     ('什', '#D32F2F'),
    
    '.md':      ('', '#FFFFFF'),
    '.txt':     ('', '#AEBBC9'),
    '.pdf':     ('', '#B30B00'),
    '.doc':     ('', '#185ABD'), '.docx':('', '#185ABD'),
    '.xls':     ('', '#207245'), '.xlsx':('', '#207245'),
    '.ppt':     ('', '#CB4A32'), '.pptx':('', '#CB4A32'),
    
    '.png':     ('', '#42A5F5'), '.jpg': ('', '#42A5F5'), '.jpeg':('', '#42A5F5'),
    '.gif':     ('', '#EA4335'), '.webp':('', '#42A5F5'),
    '.svg':     ('ﰟ', '#FFB300'),
    '.ico':     ('', '#FFC107'),
    '.mp4':     ('', '#FF6F00'), '.mkv': ('', '#FF6F00'), '.mov': ('', '#FF6F00'),
    '.mp3':     ('', '#9575CD'), '.wav': ('', '#9575CD'), '.flac':('', '#9575CD'),
    
    '.ttf':     ('', '#FF5252'), '.otf': ('', '#FF5252'), '.woff':('', '#FF5252'),
    
    '.zip':     ('', '#FBC02D'), '.rar': ('', '#FBC02D'), '.7z': ('', '#FBC02D'),
    '.tar':     ('', '#FBC02D'), '.gz':  ('', '#FBC02D'),
    '.iso':     ('', '#BDBDBD'),
    '.deb':     ('', '#A71D32'),
    '.rpm':     ('', '#D9575E'),
}

# Defaults
DIR_DEFAULT_ICON = ""
DIR_DEFAULT_COLOR = "#FFCA28"
FILE_DEFAULT_ICON = ""
FILE_DEFAULT_COLOR = "#AEBBC9"
EXEC_DEFAULT_ICON = ""
EXEC_DEFAULT_COLOR = "#00FF00"

# --- PERMISSIONS 4 PART (SUID/SGID/Sticky) ---
def get_linux_perms_4part(mode):
    if stat.S_ISDIR(mode): char_type = 'd'; color_type = "bold cyan"
    elif stat.S_ISLNK(mode): char_type = 'l'; color_type = "bold magenta"
    elif stat.S_ISSOCK(mode): char_type = 's'; color_type = "bold red"
    elif stat.S_ISFIFO(mode): char_type = 'p'; color_type = "bold yellow"
    elif stat.S_ISBLK(mode): char_type = 'b'; color_type = "bold green"
    elif stat.S_ISCHR(mode): char_type = 'c'; color_type = "bold yellow"
    else: char_type = '-'; color_type = "dim grey30"

    def check(r, w, x, s, char_s, char_S):
        res = ""
        res += "[bold green]r[/]" if r else "[dim grey30]-[/]"
        res += "[bold red]w[/]" if w else "[dim grey30]-[/]"
        if s:
            # FIX: Only RED TEXT, NO BACKGROUND
            if x: res += f"[bold red]{char_s}[/]"
            else: res += f"[bold red]{char_S}[/]"
        else:
            res += "[bold yellow]x[/]" if x else "[dim grey30]-[/]"
        return res

    u_r = bool(mode & stat.S_IRUSR); u_w = bool(mode & stat.S_IWUSR); u_x = bool(mode & stat.S_IXUSR)
    g_r = bool(mode & stat.S_IRGRP); g_w = bool(mode & stat.S_IWGRP); g_x = bool(mode & stat.S_IXGRP)
    o_r = bool(mode & stat.S_IROTH); o_w = bool(mode & stat.S_IWOTH); o_x = bool(mode & stat.S_IXOTH)
    is_suid = bool(mode & stat.S_ISUID)
    is_sgid = bool(mode & stat.S_ISGID)
    is_sticky = bool(mode & stat.S_ISVTX)

    return f"[{color_type}]{char_type}[/]{check(u_r, u_w, u_x, is_suid, 's', 'S')}{check(g_r, g_w, g_x, is_sgid, 's', 'S')}{check(o_r, o_w, o_x, is_sticky, 't', 'T')}"

# --- MAIN ---
try:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?", default=".")
    parser.add_argument("-a", "--all", action="store_true")
    parser.add_argument("-A", "--almost-all", action="store_true")
    parser.add_argument("-l", action="store_true")
    parser.add_argument("-r", "--reverse", action="store_true")
    parser.add_argument("-t", action="store_true")
    parser.add_argument("-S", action="store_true")
    parser.add_argument("--group-directories-first", action="store_true", default=True)
    args = parser.parse_args()

    target_path = os.path.abspath(args.path)
    if not os.path.exists(target_path):
        sys.exit(f"ls: cannot access '{target_path}': No such file")

    entries_list = []
    with os.scandir(target_path) as it:
        for entry in it:
            if not args.all and not args.almost_all:
                if entry.name.startswith("."): continue
            if args.almost_all and entry.name in ('.', '..'): continue
            entries_list.append(entry)

    def get_sort_key(e):
        try:
            st = e.stat(follow_symlinks=False)
            if args.t: return st.st_mtime
            if args.S: return st.st_size
            return e.name.lower()
        except: return 0

    rev = args.reverse
    if args.t or args.S: rev = not rev
    sorted_entries = sorted(entries_list, key=get_sort_key, reverse=rev)

    if args.group_directories_first:
        sorted_entries = [e for e in sorted_entries if e.is_dir(follow_symlinks=False)] + \
                         [e for e in sorted_entries if not e.is_dir(follow_symlinks=False)]

    table = Table(title=f"[bold white]LOC: [/][bold cyan]{target_path}[/]", box=box.ROUNDED, 
                  header_style=THEME["header"], border_style=THEME["border"], expand=True)
    table.add_column("PERMS", justify="left") 
    table.add_column("SIZE", justify="right", style=THEME["size"])
    table.add_column("OWNER", justify="center", style=THEME["user"])
    table.add_column("MODIFIED", justify="center")
    table.add_column("NAME", style=THEME["file"])

    for entry in sorted_entries:
        try:
            st = entry.stat(follow_symlinks=False)
            perms = get_linux_perms_4part(st.st_mode)
            size = "-" if stat.S_ISDIR(st.st_mode) else decimal(st.st_size)
            try: owner = pwd.getpwuid(st.st_uid).pw_name
            except: owner = str(st.st_uid)
            dt = datetime.datetime.fromtimestamp(st.st_mtime)
            date_str = f"[{THEME['date_day']}]{dt.strftime('%d %b')}[/] [{THEME['date_time']}]{dt.strftime('%H:%M')}[/]"
            name = entry.name
            
            # --- DISPLAY LOGIC ---
            if stat.S_ISLNK(st.st_mode):
                try: target = os.readlink(entry.path)
                except: target = "?"
                display = f"[bold cyan][/] [{THEME['symlink']}]{name}[/] [bold red]→[/] [italic cyan]{target}[/]"
            elif stat.S_ISDIR(st.st_mode):
                # Folder Logic
                icon, color = FOLDER_MAP.get(name.lower(), (DIR_DEFAULT_ICON, DIR_DEFAULT_COLOR))
                display = f"[{color}]{icon}[/] [{THEME['dir_default']}]{name}[/]"
            else:
                # File Logic
                icon, color = (None, None)
                if name.lower() in EXACT_FILE_MAP:
                    icon, color = EXACT_FILE_MAP[name.lower()]
                if not icon:
                    ext = os.path.splitext(name)[1].lower()
                    if name.lower().endswith('.d.ts'): icon, color = EXT_MAP.get('.d.ts', (None, None))
                    elif name.lower().endswith('.test.js'): icon, color = EXT_MAP.get('.test.js', (None, None))
                    else: icon, color = EXT_MAP.get(ext, (None, None))
                if not icon:
                    is_exec = bool(st.st_mode & stat.S_IXUSR)
                    icon, color = (EXEC_DEFAULT_ICON, EXEC_DEFAULT_COLOR) if is_exec else (FILE_DEFAULT_ICON, FILE_DEFAULT_COLOR)
                
                # Render
                if bool(st.st_mode & stat.S_IXUSR):
                    display = f"[{color}]{icon}[/] [bold green]{name}[/]"
                else:
                    display = f"[{color}]{icon}[/] {name}"

            table.add_row(perms, size, owner, date_str, display)
        except: pass

    console.print(table)
except Exception as e:
    console.print(f"[red]Error: {e}[/]")
EOF
