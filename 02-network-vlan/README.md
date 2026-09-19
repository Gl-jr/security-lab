# Лабораторная 02. Сеть офиса: VLAN и маршрутизация между VLAN

## Цель

Спроектировать и настроить сеть небольшого офиса: разделить отделы по VLAN,
организовать маршрутизацию между ними (router-on-a-stick), выдачу адресов по DHCP
и базовую защиту коммутатора.

## Схема

```
                     [ R1 — Cisco 2911 ]
                             │ Gi0/0  (trunk 802.1Q)
                             │
                             │ Gi0/1
                     [ SW1 — Cisco 2960 ]
       ┌──────────┬──────────┼──────────┬──────────┐
     Fa0/1      Fa0/2      Fa0/9     Fa0/10     Fa0/17
   PC-BUH1    PC-BUH2     PC-IT1     PC-IT2   PC-GUEST1
   └─ VLAN 10 ──┘          └─ VLAN 20 ──┘      VLAN 30
```

## План адресации

| VLAN | Имя | Сеть | Шлюз | Порты SW1 |
|---|---|---|---|---|
| 10 | BUH (бухгалтерия) | 192.168.10.0/24 | 192.168.10.1 | Fa0/1–8 |
| 20 | IT | 192.168.20.0/24 | 192.168.20.1 | Fa0/9–16 |
| 30 | GUEST (гости) | 192.168.30.0/24 | 192.168.30.1 | Fa0/17–20 |
| 99 | MGMT (управление) | 192.168.99.0/24 | 192.168.99.1 | — |
| 999 | NATIVE (служебный, без устройств) | — | — | trunk |

## Этапы

1. VLAN и access-порты — изоляция отделов
2. Trunk и маршрутизация между VLAN (router-on-a-stick)
3. DHCP-сервер на маршрутизаторе
4. Защита коммутатора: native VLAN, отключение неиспользуемых портов, port-security, SSH
5. Поиск неисправностей

## Ход работы

### Этап 1. VLAN и access-порты

```
enable
configure terminal
hostname SW1
vlan 10
 name BUH
vlan 20
 name IT
vlan 30
 name GUEST
exit
interface range fa0/1 - 8
 switchport mode access
 switchport access vlan 10
interface range fa0/9 - 16
 switchport mode access
 switchport access vlan 20
interface range fa0/17 - 20
 switchport mode access
 switchport access vlan 30
end
show vlan brief
write memory
```

**Результат:** _(заполнить: вывод `show vlan brief`, результаты ping)_

## Выводы

_(заполнить по итогам)_
