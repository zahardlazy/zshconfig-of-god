# 🐉 Zahard's Ultimate ZSH Configuration

A heavy-duty ZSH configuration, specifically optimized for **CTF Players**, **Pwners**, and **Red Teamers**. It comes pre-integrated with binary analysis tools, web pentest utilities, and efficient Linux system management workflows.

## 📦 Prerequisites
To ensure all commands and aliases function correctly, the following packages are required:
- **Core:** `zsh`, `oh-my-zsh`, `oh-my-posh`, `fzf`, `zoxide`, `bat`, `eza`, `neofetch`.
- **Languages:** `python3`, `pip`, `ruby`, `gem`, `node`.
- **Security Tools:** `metasploit-framework`, `nmap`, `masscan`, `gobuster`, `ffuf`, `wpscan`, `seclists`.
- **Pwn/RE:** `gdb` (pwndbg/gef), `radare2`, `cutter`, `ropgadget`, `ropper`, `one_gadget`.

---

## 🚀 Key Bindings
| Shortcut | Function | Description |
| :--- | :--- | :--- |
| `Ctrl + F` | **Find File** | Open FZF to select a file and insert its path into the current command. |
| `Ctrl + G` | **Go to Dir** | Open FZF to select a directory and `cd` into it immediately. |
| `Ctrl + R` | **History** | Search command history interactively via FZF. |
| `Ctrl + Q` | **Exit** | Replaces `Ctrl+D` to exit the shell (remapped via `stty`). |

---

## 🛠️ Command Cheat Sheet

### 1. Core System & Interface
| Command | Function |
| :--- | :--- |
| `c` | Clear screen + Show **Neofetch** (Anime Style, `NGU1.png`). |
| `zcfg` / `scfg` | Edit `.zshrc` with VSCode / Reload configuration. |
| `s` / `please` | Run with `sudo` / Re-run previous command with `sudo`. |
| `root` | Switch to root user (`sudo -i`). |
| `..` ... `.....` | Go up 1 to 4 directory levels. |
| `mkcd <dir>` | Create a directory and `cd` into it immediately. |
| `l`, `ll`, `la` | List files using **eza** (with icons, colors, git status). |
| `cat` | Use **bat** to view files (syntax highlighting). |
| `extract <file>` | Auto-extract any archive format (`.tar`, `.zip`, `.rar`, `.7z`...). |
| `ramz` | Check RAM usage and list Top 10 memory-consuming processes. |

### 2. CTF - Pwn & Reverse Engineering (Core Focus)
| Command | Detailed Description |
| :--- | :--- |
| **`bininfo <bin>`** | **All-in-one Analysis**: Shows File type, Checksec, LDD, and auto-finds offsets for `system`, `/bin/sh`, and `pop rdi` in both Binary and Libc. |
| `gdbpwn <bin>` | Run GDB in quiet mode. |
| `sec` | Check binary security features (`pwn checksec`). |
| `tplt` | Generate a quick pwntools exploit template (`exploit.py`). |
| `pattern_create` | Metasploit pattern create (`-l <length>`). |
| `pattern_offset` | Metasploit pattern offset (`-q <query>`). |
| `elfxtract` | Run ELF extraction tool (custom path). |
| `aslr_on` / `off` | Toggle System ASLR (`/proc/sys/kernel/randomize_va_space`). |
| `gcc_no_prot` | Compile with GCC disabling all protections (stack, pie) for practice. |
| `nasm_shell` | Open Ruby assembly shell code tool. |

### 3. CTF - Web & Network Recon
| Command | Function |
| :--- | :--- |
| `myip` | Show **Local** IP (Cyan) and **Public** IP (Green). |
| `webup` | Start Python HTTP Server on port 80 (for file transfer). |
| `ftpup` / `smbup`| Start FTP Server (Port 21) / SMB Server (Impacket). |
| `plzsh <port>` | Listen for Reverse Shell + Auto TTY Upgrade (Magic!). |
| `ffuf-dir` | Fuzz directories (Wordlist: directory-list-2.3-medium). |
| `ffuf-vhost` | Fuzz Subdomains/Vhosts (Wordlist: subdomains-top1million). |
| `wpscanz` | Quick WordPress Enumeration scan. |
| `wpbrute` | Brute-force WordPress XMLRPC passwords. |
| `mscanz <ip>` | Fast port scan using Masscan (Rate 1000). |
| `qmapz <ip>` | Quick Nmap scan (`-sV -sC`). |

### 4. Connectivity & VPN
| Command | Function |
| :--- | :--- |
| `vpn-htb` | Connect to HackTheBox VPN (Main). |
| `vpn-academy` | Connect to HTB Academy VPN. |
| `vpn-thm` | Connect to TryHackMe VPN. |
| `sshup` | Copy SSH connect command to **Windows Clipboard** (via OSC52). |
| `ssh2fa_on` | Enable Google Authenticator 2FA for SSH. |
| `ssh2fa_off` | Disable 2FA, revert to standard password auth. |
| `qssh` | Quick SSH using `sshpass` (skip manual password entry). |
| `rdp` | Connect RDP using `xfreerdp` (screen & clipboard config). |

### 5. Dev & Python Utils
| Command | Function |
| :--- | :--- |
| `qvenv` | Create and activate a Python virtual environment (`venv`) instantly. |
| `pipz <pkg>` | Install pip package ignoring `break-system-packages` error. |
| `pipz_upgrade` | Upgrade all pip packages. |
| `installz` | Wrapper for `sudo apt-get install -y`. |
| `docker_run` | Build and run `temp-app` container (for Web/Pwn challenges). |

### 6. Search & Find
| Command | Function |
| :--- | :--- |
| `ff <pat>` | Find file in current directory (with Code Preview). |
| `ffa <pat>` | Find file system-wide (using `locate`). |
| `fstr <str>` | Find string content **inside** files. |
| `hgrep <str>` | Grep through ZSH command history. |

### 7. Fun & Misc
| Command | Function |
| :--- | :--- |
| `shimeji` | Summon Arknights characters to run on your desktop (Shijima-Qt). |
| `niggamode` | Switch to **TTY3** (Void mode / Black screen for focus). |
| `godmode` | Switch back to Graphical Interface (GUI). |
| `thunar` | Open GUI File Manager (`&` background). |

---

## ⚙️ Configuration Notes
*Attention: Some aliases point to hardcoded paths specific to the author's machine. Please update `.zshrc` if copying to a new system:*
* **VPN:** `/home/crystal/Documents/*.ovpn` -> Update to your username/path.
* **Tools:** `~/apps/...` (android-studio, jwt_tool, tplmap, etc.).
* **IDA/Cutter:** `/home/zahard/...` -> Point to your installation directory.

## 🎨 Credits
* **Theme:** Oh My Posh (LambdaGeneration).
* **Shell:** ZSH + Oh My Zsh.
* **Author:** Zahard (Mlô).
