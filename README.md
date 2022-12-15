# ClosX

## Command Line Operation
```
  3 Tier Clos Fabric Generator
  Example usage:
  $ cd ClosX
  $ chmod +x closx
  $ ./closx -spine 8 -tier1 16 -tier2 16 -ipr 10.0.0.0/22 -mgmtr 172.16.0.0/24 -vendor junos
  $ ./closx -spine 8 -tier1 16 -tier2 16 -ipr 10.0.0.0/22 -mgmtr 172.16.0.0/24 -vendor cisco_ios

    -spine: size of spine
    -t2: size of tier 2
    -t1: size of tier 1
    -ipr: IP range to extract /31 p2p IPs from
    -mgmtr: IP range to extract /32 management IPs from
    -vendor: vendor template to render configuration against

  Currently supported vendor platforms:
    - Junos
    - Cisco IOS
```
## 3 Tier Clos Example - 6 wide spine | 10 wide tier 2 | 10 wide tier 1
![3 Tier Clos - 6 wide spine | 10 wide tier 2 | 10 wide tier 1](https://github.com/byMacf/ClosX/blob/main/6widespine_10widetier2_10widetier1_clos.png?raw=true)

## 3 Tier Clos Example - 8 wide spine | 16 wide tier 2 | 16 wide tier 1
![3 Tier Clos - 8 wide spine | 16 wide tier 2 | 16 wide tier 1](https://github.com/byMacf/ClosX/blob/main/8widespine_16widetier2_16widetier1_clos.png?raw=true)
