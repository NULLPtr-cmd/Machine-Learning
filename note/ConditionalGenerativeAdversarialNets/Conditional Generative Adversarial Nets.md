# Conditional Generative Adversarial Nets

Author: Zhang Xiaozheng Date: 2019/11/28

In generative adversarial nets, we can generate the pictures which is very realistic. But there is some problems which is we can't control the mode of these generative pictures. 

So to get the picture we want, this paper use the conditional generative adversarial nets. In generative adversarial nets, we change the function to
$$
min_Gmax_D \   V(G,D)=E_{x\sim p_{data}}[log(D(x|y))]+E_{z\sim p_z}[log(1-log(G(z|y)))]
$$
So this paper simply fed the label *y* to the nets.



