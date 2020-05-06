# handson_pytorch

このリポジトリはPytorchのハンズオンのためのノートブックが含まれます。ノートブックはGoogle colaboratory上で動作確認しています。

## Notebooks
* https://colab.research.google.com/github/PyDataOsaka/handson_pytorch/blob/master/linear_regression.ipynb
* https://colab.research.google.com/github/PyDataOsaka/handson_pytorch/blob/master/cnn_gpu.ipynb
* https://colab.research.google.com/github/PyDataOsaka/handson_pytorch/blob/master/resnet18_gpu.ipynb
* https://colab.research.google.com/github/PyDataOsaka/handson_pytorch/blob/master/resnet18_tpu.ipynb

## References
* [Training a classifier](https://pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html)
* [Pytorch on XLA devices](http://pytorch.org/xla/release/1.5/index.html)
* [pytorch / xla](https://github.com/pytorch/xla/)
* [【秒速で無料GPUを使う】深層学習実践Tips on Colaboratory](https://qiita.com/tomo_makes/items/b3c60b10f7b25a0a5935)
* [Residual Network(ResNet)の理解とチューニングのベストプラクティス](https://deepage.net/amp/deep_learning/2016/11/30/resnet/)
* [Google ColabのTPUで対GPUの最速に挑戦する](https://qiita.com/koshian2/items/fb989cebe0266d1b32fc)

## Performance comparison on ResNet18

* CPU

```
Elapsed time: 15.5 [sec] for 5 stes
(310.4 [sec] for 100 steps)
```

* GPU

```
[1,   100] loss: 0.100, elapsed time: 9.0 [sec]
[1,   200] loss: 0.080, elapsed time: 9.2 [sec]
[1,   300] loss: 0.072, elapsed time: 9.6 [sec]
[1,   400] loss: 0.066, elapsed time: 9.4 [sec]
[1,   500] loss: 0.063, elapsed time: 9.1 [sec]
[1,   600] loss: 0.057, elapsed time: 8.9 [sec]
[1,   700] loss: 0.054, elapsed time: 8.8 [sec]
[2,   100] loss: 0.087, elapsed time: 16.0 [sec]
[2,   200] loss: 0.044, elapsed time: 8.8 [sec]
[2,   300] loss: 0.043, elapsed time: 8.9 [sec]
[2,   400] loss: 0.040, elapsed time: 9.0 [sec]
[2,   500] loss: 0.039, elapsed time: 9.0 [sec]
[2,   600] loss: 0.039, elapsed time: 9.0 [sec]
[2,   700] loss: 0.036, elapsed time: 9.0 [sec]
```

* TPU

```
[1,   100] loss: 0.098, elapsed time: 15.8 [sec]
[1,   200] loss: 0.082, elapsed time: 6.8 [sec]
[1,   300] loss: 0.075, elapsed time: 6.9 [sec]
[1,   400] loss: 0.067, elapsed time: 6.9 [sec]
[1,   500] loss: 0.062, elapsed time: 6.9 [sec]
[1,   600] loss: 0.059, elapsed time: 6.9 [sec]
[1,   700] loss: 0.054, elapsed time: 6.8 [sec]
[2,   100] loss: 0.088, elapsed time: 15.5 [sec]
[2,   200] loss: 0.046, elapsed time: 6.8 [sec]
[2,   300] loss: 0.044, elapsed time: 6.7 [sec]
[2,   400] loss: 0.041, elapsed time: 6.9 [sec]
[2,   500] loss: 0.039, elapsed time: 6.7 [sec]
[2,   600] loss: 0.039, elapsed time: 6.8 [sec]
[2,   700] loss: 0.037, elapsed time: 6.8 [sec]
```
