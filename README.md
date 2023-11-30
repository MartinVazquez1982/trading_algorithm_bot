# Trading Algorithm BOT

Bot de trading desarrollado por David Burckhardt y Martin Vazquez Arispe, estudiantes de Ingeniería de Sistemas en la UNICEN.
Es el proyecto final de la materia optativa Introducción al trading algorítmico.

## Indice

1. [Introducción](#introducción)
2. [Instalación del Bot](#instalación-del-bot)
3. [Ejecucion del Bot](#ejecucion-del-bot)

## Introducción

Este bot fue desarrollado en python mediante el framework Backtrader con un fin academico y utiliza datos historicos para realizar la simulación.

El bot cuenta con varias estrategias que se encuentran dentro del directorio *Strategies*, que se compone de la siguiente forma:

```
Strategies
|-- Simple_Strategies
    |-- bollinger.py
    |-- crossMethod.py
    |-- deathCross.py
    |-- firstStrategy.py
    |-- goldenCross.py
    |-- MACD.py
    |-- RSI.py
|-- Combined_Strategies
    |-- strategy_general.py
    |-- strategy_1.py
    |-- strategy_2.py
|-- Main_Strategies
    |-- strategy_final.py
```

La estrategia que utiliza por defecto es *strategy_final.py* la cual emplea varias tecnicas para determinar si ocurre una señal de compra o una señal de venta

## Instalación del Bot

Para poder correr el Bot se requiere tener instalado una version de python superior o igual a la 3.2. Y luego instalar backtrader mediante el siguiente comando:

```bash
pip install backtrader[plotting]
```
Con esto ya se encuentra listo para ejecutar.

## Ejecucion del Bot

Para ejecutar el bot se tiene que correr el archivo:

```
Trading_Algorithm_bot
|-- run_bot.py
```

Se recomienda ejecutar por consola dado que espera el datafeed a utilizar por argumento, sino por defecto utiliza oracle.

Datafeeds:
- ORCL => Oracle
- NVDA => NVIDIA
- YHOO => Yahoo
- KO => Coca Cola
- BMA => Banco Macro

comando para ejecutar por consola:

```bash
python run_bot.py [datafeed]
```