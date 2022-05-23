# SrotoAPP
Program pro automatizaci plnění pdf formulářů

Požadavky: 
  - Python 3.0+

Jak program funguje a co je nutné dodržet:
 - program čte z csv souboru hlavičku a pak následně data, které jsou zařazeny do datagridu 
 - z tohoto datagridu jsou následně přečteny zkryté proměnné v pdf formuláři a napárovány ke správným datům odpovídajícím v csv tabulce 
 - nutné dodržet formáty 
 - veškeré konvertovací funkce jsou již zabudováný do programu 

Příklady: 
 - máme xls tabulku a tu potřebujeme převést do csv
 - provedeme to integrovaným nástrojem v naší aplikaci, která to přesně zformátuje na požadovaný formát 
 - musíme mít připravený pdf fomulář (dá se vytvořit za pomocí adobe acrobat pro nebo jinou alternativou) 
 - v pdf fomuláři musíme mít názvy buněk (tyto proměnné nejsou viditelné což je pro nás výhodné) 
 - po výběru správných souborů můžeme spustit plnič a je hotovo 
  
ToDo: 
 - vytvořit autoupdate
 - autoskripty pro instalaci programu 
 
 Nice to have: 
 - web interface namísto konzole
 
