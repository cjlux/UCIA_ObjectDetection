# Aseba bytecode assembler

A simple assembler is provided for the Aseba virtual machine (VM). The assembler input can contain VM instructions, labels, symbols, expressions, pseudo-instructions, and comments.

The Aseba VM has three separate memory spaces: program (where bytecode is stored), data (where variables are stored, including those predefined and accessed also by the firmware for I/O), and stack. The stack is used for return addresses of subroutine calls, for passing arguments and getting results of arithmetic, logic and load/store operators, and for passing parameter addresses to native functions. All values (instructions, data and stack elements) are stored in 16-bit words. Arithmetic and comparison operators assume signed values. Some instructions contain in their least-significant 12 bits a signed value for addresses, ids, relative jumps, or small literal values.

Communication between programs and the robot hardware is performed with two means: via special variables, and via calls to native functions. Special variables are located at the beginning of the data space. Native functions, identified by an id, expect parameter addresses on the stack; the native function itself removes these addresses from the stack.

The bytecode begins with a table at address 0 with the addresses of event handlers. The first word is the total table length (always odd); then each entry is made of two words, first the event id, then the address in the program. When the VM receives an event, it checks in the table if it finds an entry for it; in that case, it jumps to the specified address and runs the code until a "stop" instruction. Variables are preserved across event handling. A special event (id 0xffff or -1) corresponds to initialization; it is triggered upon program start.

The location of special variables, the id of native functions and of events depend on the robot and are subject to change between firmware releases. Symbols are predefined to use values obtained from the robot itself (see below).

## Assembler input syntax

An assembler line can contain a label followed by a colon, an instruction or pseudo-instruction with its comma-separated or space-separated arguments, and a comment. Any or all of these elements can be missing. Arguments can be numbers in decimal or hexadecimal (prefixed with 0x), constants, or arithmetic expressions made of numbers, constants, and + and - operators, without space or parentheses. Constants are defined as labels or with the pseudo-instruction equ (see below). They can be used before their definition.

Examples:
```
loop: push 123  ; some comment
loop: push 123
loop:
      push 123
````

## Pseudo-instructions

Constants, useful mainly for the initial event table:
```
dc val1, val2, ...
````

Symbol definition:
```
symbol: equ value
```

Instructions
------------

Push a 12-bit signed value onto the stack

	push.s value

Push a 16-bit signed value onto the stack

	push value

Push a value fetched at a fixed address

	load address

Pop a value and store it at a fixed address

	store address

Pop a value, add it to a fixed address, fetch the value there and push it onto the stack

	load.ind address


Pop a value, add it to a fixed address, pop a second value and store it there

	store.ind address

Change the sign of the top stack element

	neg

Take the absolute value of the top stack element

	abs

Take the one's complement of the top stack element

	bitnot

Take the logical _not_ of the top stack element (not implemented in the VM, _must not be used_)

	not

Pop 2 elements a and b and push a << b (`a` shifted to the left by `b` bits)

	sl

Pop 2 elements a and b and push a >> b (arithmetic shift right, i.e. signed division by a power of 2: `a` shifted to the right by `b` bits with sign bit replicated)

	asr

Pop 2 elements `a` and `b` and push `a + b`

	add

Pop 2 elements `a` and `b` and push `a - b`

	sub

Pop 2 elements `a` and `b` and push `a * b`

	mult

Pop 2 elements `a` and `b` and push `a / b`

	div

pop 2 elements `a` and `b` and push `a % b` (the remainder of `a` divided by `b`)

	mod

pop 2 elements `a` and `b` and push `a | b` (bitwise or)

	bitor

pop 2 elements `a` and `b` and push `a ^ b` (bitwise exclusive or)

	bitxor

pop 2 elements `a` and `b` and push `a & b` (bitwise and)

	bitand

pop 2 elements `a` and `b` and push 1 if `a == b`, 0 otherwise

	eq

pop 2 elements `a` and `b` and push 1 if `a != b`, 0 otherwise

	ne

pop 2 elements `a` and `b` and push 1 if `a > b`, 0 otherwise

	gt

pop 2 elements `a` and `b` and push 1 if `a >= b`, 0 otherwise

	ge

pop 2 elements `a` and `b` and push 1 if `a < b`, 0 otherwise

	lt

pop 2 elements `a` and `b` and push 1 if `a <= b`, 0 otherwise

	le

pop 2 elements `a` and `b` and push 1 if `a` or `b != 0`, 0 otherwise

	or

pop 2 elements `a` and `b` and push 1 if `a` and `b != b`, 0 otherwise

	and

go to the specified absolute address in the bytecode

	jump address

pop 2 elements, apply a condition to them (one of the logical operators `eq`, `ne`, `gt`, `ge`, `lt`, `le`, `or`, `and`), and go to the specified absolute address if the result is false (0)

	jump.if.not condition address

pop 2 elements and apply a condition to them (one of the logical operators `eq`, `ne`, `gt`, `ge`, `lt`, `le`, `or`, `and`); if the result is false (0), go to that address and modify the instruction to `dont.jump.when.not`. This is used to implement the `when` Aseba statement.

	do.jump.when.not condition address

pop 2 elements and apply a condition to them (one of the logical operators `eq`, `ne`, `gt`, `ge`, `lt`, `le`, `or`, `and`); if the result is true (not 0), modify the instruction to `do.jump.when.not`. This is the `do.jump.when.not` instruction once it has been triggered.

	do.jump.always condition address

emit an event with the specified identifier and data at the specified address with the specified size

	emit id, address, size

call the native function specified by its id

	callnat id

call a subroutine at the specified absolute address in the bytecode

	callsub address

return from a subroutine (pop an address from the stack and go there)

	ret

## Predefined definitions

The set of definitions contains predefined values for the variables, native functions and events, retrieved from the Thymio. Variables have the same name as in Aseba. Two special definitions characterize the area of memory available for user variables:

`_userdata`: address of the first word available for user variables

`_topdata`: address following the last word available for user variables

The id of native functions is the same as the name used in Aseba, prefixed with `_nf.` to avoid any name clash with variables.

The id of local events is the same as the name used in Aseba, prefixed with `_ev.` to avoid any name clash with variables. The id of the event corresponding to the start of the program is named `_ev.init`

Here is the complete list, as of November 2020. It isn't coded in the Python module, but retrieved from the Thymio because the exact values depend on the firmware version.

```
_id:
	equ 0
event.source:
	equ 1
event.args:
	equ 2
_fwversion:
	equ 34
_productId:
	equ 36
buttons._raw:
	equ 37
button.backward:
	equ 42
button.left:
	equ 43
button.center:
	equ 44
button.forward:
	equ 45
button.right:
	equ 46
buttons._mean:
	equ 47
buttons._noise:
	equ 52
prox.horizontal:
	equ 57
prox.comm.rx._payloads:
	equ 64
prox.comm.rx._intensities:
	equ 71
prox.comm.rx:
	equ 78
prox.comm.tx:
	equ 79
prox.ground.ambiant:
	equ 80
prox.ground.reflected:
	equ 82
prox.ground.delta:
	equ 84
motor.left.target:
	equ 86
motor.right.target:
	equ 87
_vbat:
	equ 88
_imot:
	equ 90
motor.left.speed:
	equ 92
motor.right.speed:
	equ 93
motor.left.pwm:
	equ 94
motor.right.pwm:
	equ 95
_integrator:
	equ 96
acc:
	equ 97
leds.top:
	equ 100
leds.bottom.left:
	equ 103
leds.bottom.right:
	equ 106
leds.circle:
	equ 109
temperature:
	equ 117
rc5.address:
	equ 118
rc5.command:
	equ 119
mic.intensity:
	equ 120
mic.threshold:
	equ 121
mic._mean:
	equ 122
timer.period:
	equ 123
acc._tap:
	equ 125

_userdata:
	equ 126
_topdata:
	equ 620

_nf._system_reboot:
	equ 0
_nf._system_settings_read:
	equ 1
_nf._system_settings_write:
	equ 2
_nf._system_settings_flash:
	equ 3
_nf.math.copy:
	equ 4
_nf.math.fill:
	equ 5
_nf.math.addscalar:
	equ 6
_nf.math.add:
	equ 7
_nf.math.sub:
	equ 8
_nf.math.mul:
	equ 9
_nf.math.div:
	equ 10
_nf.math.min:
	equ 11
_nf.math.max:
	equ 12
_nf.math.clamp:
	equ 13
_nf.math.dot:
	equ 14
_nf.math.stat:
	equ 15
_nf.math.argbounds:
	equ 16
_nf.math.sort:
	equ 17
_nf.math.muldiv:
	equ 18
_nf.math.atan2:
	equ 19
_nf.math.sin:
	equ 20
_nf.math.cos:
	equ 21
_nf.math.rot2:
	equ 22
_nf.math.sqrt:
	equ 23
_nf.math.rand:
	equ 24
_nf._leds.set:
	equ 25
_nf.sound.record:
	equ 26
_nf.sound.play:
	equ 27
_nf.sound.replay:
	equ 28
_nf.sound.system:
	equ 29
_nf.leds.circle:
	equ 30
_nf.leds.top:
	equ 31
_nf.leds.bottom.left:
	equ 32
_nf.leds.bottom.right:
	equ 33
_nf.sound.freq:
	equ 34
_nf.leds.buttons:
	equ 35
_nf.leds.prox.h:
	equ 36
_nf.leds.prox.v:
	equ 37
_nf.leds.rc:
	equ 38
_nf.leds.sound:
	equ 39
_nf.leds.temperature:
	equ 40
_nf.sound.wave:
	equ 41
_nf.prox.comm.enable:
	equ 42
_nf.sd.open:
	equ 43
_nf.sd.write:
	equ 44
_nf.sd.read:
	equ 45
_nf.sd.seek:
	equ 46
_nf._rf.nodeid:
	equ 47
_nf._poweroff:
	equ 48

_ev.init:
    equ 65535
_ev.button.backward:
    equ 65534
_ev.button.left:
    equ 65533
_ev.button.center:
    equ 65532
_ev.button.forward:
    equ 65531
_ev.button.right:
    equ 65530
_ev.buttons:
    equ 65529
_ev.prox:
    equ 65528
_ev.prox.comm:
    equ 65527
_ev.tap:
    equ 65526
_ev.acc:
    equ 65525
_ev.mic:
    equ 65524
_ev.sound.finished:
    equ 65523
_ev.temperature:
    equ 65522
_ev.rc5:
    equ 65521
_ev.motor:
    equ 65520
_ev.timer0:
    equ 65519
_ev.timer1:
    equ 65518
```
