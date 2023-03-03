# Drawer Pico

A library that simulates renderings of 3D figures on SSD1306 128x64 displays module running on Raspberry Pi Pico.

https://user-images.githubusercontent.com/80235345/222620217-a5fae7ae-37f3-46aa-a1b1-af97441f22ea.mp4

## You will need...

- Basic knowledges about Python and SSD1306 basic usage with Raspberry Pi Pico
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

## First Usage

You can run `main.py` file and you can see running the **animation test**.

## How to Create a simple Figure

> We will create a square to facilitate the explanations

In 3D space we have three coordinates `x`, `y` and `z`.

For this example, we begin creating a square of 1x1 size.

First at all, you need to define its coordinates.

![](https://user-images.githubusercontent.com/80235345/222619072-436f3022-1c03-45e1-b82e-dc9c1b1813c0.png)

> Remember, you are in the 3D space.

`drawer pico` works like a pencil in a paper, you need to indicate where begin and where finish.

For example, if we want begin in `x=-1`, `y=1`, `z=1` and finish in the same location, we need some like this:

```
=== Let's draw! ===

Put our pencil in 	-1, 1, 0
and go to 		 1, 1, 0
and go to		 1, -1, 0
and go to		-1, -1, 0
and go to		-1, 1, 0

=== Stop drawing. ===
```

![draw-step-by-step](https://user-images.githubusercontent.com/80235345/222619385-e75651f1-bb39-49e3-b558-430c71cce646.png)

We need to say that to our `main.py` file. You can create a `json` file, so the `drawer` will know where to draw.

```json
{
    "shapes": {
        "square": {
            "coordinates": [
		-1, 1, 0,
		1, 1, 0,
		1, -1, 0,
		-1, -1, 0,
		-1, 1, 0
            ]
        }
    }
}
```

Once you create your `json` file, we need to import on your `main.py` file:

```python
# Reading the figures file
with open('square.json', 'r+') as file:
    data = json.load(file)

square = Drawer(oled, data) # Creating object Drawer
```
> You can repeat above steps for all figures as you want.

It's ready!, now, you can use some methods like `rotate`, `move` and `resize`.

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

square.move('square', mx, my, mz)
```

### Resize

```python
# sx: increase/decrease x-axis size
# sy: increase/decrease y-axis size
# sz: increase/decrease z-axis size

square.resize('square', sx, sy, sz)
```
