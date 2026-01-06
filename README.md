# 🐉 Zahard's Ultimate ZSH Configuration

A heavy-duty, highly customized ZSH configuration optimized for **CTF Players**, **Binary Exploitation (Pwn)**, and **Red Teamers**.

This config integrates powerful aliases for binary analysis, web reconnaissance, and system management, wrapped in a beautiful **Oh My Posh** theme.

---

## 📦 Installation & Dependencies

To ensure all aliases (like `bininfo`, `ff`, `sshup`) work without errors, follow these setup steps.

### 1. Core Shell Environment
* **Shell:** ZSH (`sudo apt install zsh`)
* **Framework:** [Oh My Zsh](https://ohmyzsh.github.io/)
* **Theme:** [Oh My Posh](https://ohmyposh.dev/) (Config: `~/.oh-my-posh/themes/lambdageneration.omp.json`)
* **Plugins:** `git`, `zsh-autosuggestions`, `zsh-syntax-highlighting`.

### 2. System Utilities (APT)
Install the core CLI tools required for file listing, searching, and visuals:
```bash
sudo apt update && sudo apt install -y \
    bat eza fdfind ripgrep plocate \
    curl wget git xclip xsel \
    python3-venv python3-pip ruby-full nodejs \
    net-tools sshpass proxychains4 xfreerdp \
    p7zip-full unrar cabextract \
    thunar wmctrl neofetch
```

### 3. Hacking Tools (Kali/APT)
Standard security tools used in the aliases:
```bash
sudo apt install -y \
    nmap masscan gobuster ffuf wpscan \
    metasploit-framework exploitdb \
    gdb checksec nasm radare2
```

### 4. Python Libraries (PIP)
Required for Pwn and Web tools. Note: `pipz` alias uses `--break-system-packages`.
```bash
pip install --break-system-packages \
    pwntools impacket pyftpdlib \
    wsgidav ropper ropgadget one_gadget
```

### 5. Custom Tools Layout
The config expects specific tools in specific folders. Clone these if you want the aliases (`enum4linux`, `pwninit`, `jwt_tool`, etc.) to work:

* **`~/apps/`**: `up-http-tool`, `subbrute`, `tplmap`, `XSStrike`, `EyeWitness`, `jwt_tool`, `android-studio`.
* **`~/tools/`**: `pwninit-py`.
* **`~/Desktop/scripts/`**: `enum4linux-ng`, `wesng`.
* **`./Shijima-Qt/`**: Desktop mascot (Arknights).

---

## 🚀 Key Bindings & Navigation

| Shortcut | Function | Description |
| :--- | :--- | :--- |
| **Ctrl + F** | `fzf-file-widget` | Insert file path into command line. |
| **Ctrl + G** | `fzf-cd-widget` | CD into selected directory immediately. |
| **Ctrl + R** | `fzf-history-widget` | Interactive History Search. |
| **Ctrl + Q** | **Exit** | Remapped Exit key (replaces `Ctrl+D`). |
| `c` | **Clear** | Clear screen + Anime Neofetch. |
| `..` to `.....`| **Up** | Go up 1-4 directory levels. |
| `mkcd <dir>` | **Make & Go** | Create directory and `cd` into it. |

---

## 🛠️ Command Cheat Sheet

### 💀 CTF - Pwn & Reverse Engineering (Focus)
| Command | Description |
| :--- | :--- |
| **`bininfo <bin>`** | **Automated Analysis:** Shows file type, checksec, ldd, and finds offsets for `system`, `/bin/sh`, and `pop rdi` (Binary & Libc). |
| `gdbpwn <bin>` | Run GDB in quiet mode (`gdb -q`). |
| `sec` | Run `pwn checksec`. |
| `tplt` | Generate `exploit.py` template using pwntools. |
| `pattern_create` | Metasploit pattern create (`-l length`). |
| `pattern_offset` | Metasploit pattern offset (`-q query`). |
| `elfxtract` | Run `elfxtract` tool. |
| `aslr_off` / `on` | Toggle ASLR (Requires sudo). |
| `gcc_no_prot` | Compile with NO protections (Stack/PIE/NX off). |
| `xmod` | Auto `chmod +x` all ELF files in current dir. |
| `ida` / `ghidra` | Launch IDA Pro / Ghidra scripts. |

### 🌐 CTF - Web & Network
| Command | Description |
| :--- | :--- |
| `myip` | Show Local (Cyan) & Public (Green) IPs. |
| `webup` | Python HTTP Server (Port 80). |
| `ftpup` / `smbup` | Start FTP (21) / SMB Server (Impacket). |
| `plzsh <port>` | **Reverse Shell Listener:** Spawns listener + upgrades TTY automatically. |
| `sshup` | **Clipboard Magic:** Copy SSH connect string to Windows Clipboard (OSC52). |
| `ssh2fa_on` | Enable Google Authenticator 2FA for SSH. |
| `vpn-htb` | Connect to HackTheBox VPN. |
| `vpn-thm` | Connect to TryHackMe VPN. |

### 🔍 Search & Find (Powered by FZF)
| Command | Description |
| :--- | :--- |
| `ff <pattern>` | Find file in current dir (includes **Code Preview**). |
| `ffa <pattern>` | Find file system-wide (using `locate`). |
| `fstr <str>` | Find string content **inside** files (Recursive). |
| `hgrep <str>` | Grep through ZSH history. |

### ⚔️ Scanners & Enumeration
| Command | Description |
| :--- | :--- |
| `ffuf-dir` | Fuzz directories (Medium wordlist). |
| `ffuf-vhost` | Fuzz vhosts (Top 1M wordlist). |
| `wpscanz` | Quick WPScan enumeration. |
| `mscanz <ip>` | Masscan (Rate 1000). |
| `qmapz <ip>` | Nmap (`-sV -sC`). |
| `nse <grep>` | Search Nmap scripts. |

### 💻 Dev & System Utils
| Command | Description |
| :--- | :--- |
| `qvenv` | Create & activate Python `venv`. |
| `pipz` | `pip install` (ignoring system break error). |
| `pipz_upgrade` | Upgrade all pip packages. |
| `installz` | Alias for `sudo apt install -y`. |
| `docker_run` | Build & run `temp-app` container. |
| `ramz` | Show RAM usage & Top 10 processes. |
| `extract` | Universal archive extractor (`.tar`, `.zip`, `.rar`, etc.). |

---

## ⚙️ Configuration Notes
> **⚠️ Hardcoded Paths:**
> This config contains paths specific to the author's machine. Please update `.zshrc` to match your user:
> * **VPNs:** `/home/crystal/Documents/*.ovpn`
> * **Tools:** `/home/zahard/apps/...` or `/home/zahard/ida-pro-9.0/`

## 🎨 Fun Features
* **`shimeji`**: Spawns Arknights desktop pets (requires Shijima-Qt).
* **`niggamode`**: Switches to TTY3 (Black screen mode).
* **`godmode`**: Returns to GUI (TTY2/1).

---
**Author:** Zahard (Mlô)
