# Drawer Pico

A library that simulates renderings of 3D figures on SSD1306 128x64 displays module running on Raspberry Pi Pico.

![Cube example](images/example.gif){ width=60% }

## You will need...

- Basic knowledges about Python and electronic circuits.
- Raspberry Pi Pico.
- SSD1306 128x64 0.9".
- Protoboard.
- Jumpers / wires.
- Thonny's Python IDE.

## Installation

Download this repo and import all files in your Pico using Thonny's IDE.

Inside your Pico, your files should look like this:

```bash
.
├── cube.json
├── figures.json
├── lib
│   ├── drawer.py
│   └── ssd1306.py
├── line.json
└── main.py
```

## Usage

You can run `main.py` file and you can see running the animation test:

![](image/example.gif){ width=60% }

## How to Import a 3D Figure

In 3D space we have three coordinates `x`, `y` and `z`.

For this example, we begin creating a square of 2x2 size.

First at all, you need to define its coordinates in a plane.

![](image/example-create-quare.png){ width=60% }

`drawer pico` works like a pencil in a paper, you need to indicate where begin and where finish.

For example, if we want begin in `x:-2`, `y:2`, our path looks like this:

```
=== Let's draw! ===

Put our pencil in 	-2, 2
and go to 			 2, 2
go to				 2, -2
go to				-2, -2
go to				-2, 2

=== Stop drawing. ===
```

We need to say that to our `main.py` file. So, you can create a `json` file para que el `drawer` sepa donde dibujar.

```json
{
    "shapes": {
        "square": {
            "coordinates": [
				-2, 2, 0,
				2, 2, 0,
				2, -2, 0,
				-2, -2, 0,
				-2, 2, 0
            ]
        }
    }
}
```

Once you create your `json` file, we need to import on your `main.py` file:

```python
# Reading the figures file
with open('cube.json', 'r+') as file:
    data = json.load(file)

square = Drawer(oled, data) # Creating object Drawer
```

It's ready!, now, you can use some methods like `rotate`, `move` and `resize`.

![](image/example){ width=60% }

## Methods

### Rotate

```python
# rx: x-axis rotation
# ry: y-axis rotation
# rz: z-axis rotation

square.rotate('square', rx, ry, rz)
```

### Move

```python
# mx: move mx distance in x-axis
# my: move my distance in y-axis
# mz: move mz distance in z-axis

square.move('cube', mx, my, mz)
```

### Resize

```python
# sx: increase/decrease x-axis size
# sy: increase/decrease y-axis size
# sz: increase/decrease z-axis size

square.resize('cube', sx, sy, sz)
```
