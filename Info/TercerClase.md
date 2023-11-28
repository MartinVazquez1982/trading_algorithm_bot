# Trading Algorith - BOT

## Instalacion del Framework

```bash
pip install backtrader[plotting]
```
## Desarrollo

Importar backtrader para poder utilizar el framework

```python
import backtrader as bt
```
El bloque que asegura que el código dentro de él solo se ejecutará cuando se ejecute el script directamente, no cuando se importe como un módulo.

```python
if __name__ == '__main__':
```
Esta línea crea una instancia de la clase *Cerebro*, que es el motor principal para el backtesting y el trading en vivo en Backtrader.

```python
cerebro = bt.Cerebro()
```
Se establece el saldo de efectivo inicial para la cuenta de trading en 100.000.

```python
cerebro.broker.setcash(100000.0)
```

Se imprime con cuanto se inicia el trading

```python
print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
```

Se ejecuta la simulación de backtesting, ejecutando las estrategias y analizadores que se han agregado al motor Cerebro.

```python
cerebro.run()
```

Finalmente se muestra el resultado de las inversiones realizadas

```python
print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
```
Se obtiene la ruta del archivo que se utilizara para el backtesting

```python
datapath = os.path.join(r".\\Data\\orcl-1995-2014.txt")
```
Este bloque de código crea un feed de datos usando la clase *YahooFinanceCSVData* de la biblioteca *backtrader*. El feed de datos cargará datos históricos de Yahoo Finance para el nombre de datos especificado (*datapath*) y el período de tiempo (*fromdate* a *todate*). El parámetro *reverse* se establece en *False*, lo que significa que los datos se cargarán en orden cronológico.

```python
# Crear un feed de datos
data = bt.feeds.YahooFinanceCSVData(
    dataname=datapath,
    # No pasar valores antes de esta fecha
    fromdate=datetime.datetime(2000, 1, 1),
    # No pasar valores después de esta fecha
    todate=datetime.datetime(2000, 12, 31),
    reverse=False)
```
Agrega el feed de datos al motor Cerebro. Esto hará que los datos estén disponibles para las estrategias que se agregan al motor Cerebro.

```python
# Agregar el feed de datos a Cerebro
cerebro.adddata(data)
```
Agrega la clase *TestStrategy* al motor Cerebro. Esto significa que *TestStrategy* se utilizará para analizar los datos del feed de datos.

```python
cerebro.addstrategy(fs.TestStrategy)
```
Esta clase define una estrategia de trading llamada TestStrategy, que hereda de la clase bt.Strategy de Backtrader. La clase TestStrategy contiene dos métodos: log() y init().

```python
class TestStrategy(bt.Strategy):
```

## Clase Strategy de Backtrader

Metodos y atributos mas importantes:

El método *init()* es el método constructor de la clase Strategy. Se llama cuando se crea una instancia de la clase *Strategy*. El método *init()* se utiliza para inicializar los parámetros de la estrategia de trading y para establecer cualquier otra configuración necesaria.

```python
__init__(self):
```

El método *next()* se llama en cada modificacion de la market data. Este es el lugar donde se implementa la lógica de la estrategia de trading. El método *next()* puede utilizarse para realizar operaciones de trading, calcular indicadores técnicos o simplemente registrar datos.

```python
next(self)
```

El método *stop()* se llama cuando se detiene la estrategia de trading. Este es el lugar donde se pueden realizar acciones de limpieza, como cerrar las posiciones abiertas.

```python
stop(self)
```

El atributo *params* es un diccionario que contiene los parámetros de la estrategia de trading. Los parámetros de la estrategia de trading son variables que se pueden configurar para controlar el comportamiento de la estrategia.

```python
self.params
```

El atributo *datas* es una lista de objetos *DataSeries* que representan los datos utilizados por la estrategia de trading. Los objetos *DataSeries* proporcionan acceso a los datos de precios, volumen y otros datos relevantes para el trading.

```python
self.datas
```

El atributo *broker* es un objeto *Broker* que se utiliza para realizar operaciones de trading. El objeto *Broker* proporciona métodos para realizar operaciones de compra, venta, cierre de posiciones y otras operaciones de trading.

```python
self.broker
```
El atributo *analyzers* es una lista de objetos *Analyzer* que se utilizan para analizar el rendimiento de la estrategia de trading. Los objetos *Analyzer* proporcionan información sobre el rendimiento de la estrategia, como las ganancias, las pérdidas y la rentabilidad.

```python
self.analyzers
```