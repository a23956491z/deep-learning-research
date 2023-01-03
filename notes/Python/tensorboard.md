local side
```bash
ssh -L 16006:127.0.0.1:6006 divclab@134.208.3.186 
```
`127.0.0.1:16006`

server side
```bash
tensorboard --logdir='tfboard'
```