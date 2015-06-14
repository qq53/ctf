url: http://ctf.idf.cn/index.php?g=game&m=article&a=index&id=57

0x00: 封包找出邮件附件 共5个包 发现大小525701

0x01: 发现导出到5个包大小527521，打开第一个发现364偏移开始才是RAR头

0x02: 于是dd if=1 of=1.1 bs=1 skip=364

0x03: 合成后解压，发现无法解压，要密码，把23偏移从0x84改成0x80

0x04: 解压是个PE，BINWALK解压最后一个图片，扫描即可
