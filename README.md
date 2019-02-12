# CM202 Project 2
For this project we are required to set up an RNN and an autoencoder. 

##RNN 
For our RNN we decided to generate video game reviews. To do this, we use hunkim's word level rnn. https://github.com/hunkim/word-rnn-tensorflow

The dataset we chose is 231780 video game reviews from jmcauley's amazon product dataset http://jmcauley.ucsd.edu/data/amazon/. This dataset has some formating errors, so beware that you will need to reformat the json in order to use it as expected. 

Of these reviews there are 14853 1 star reviews (the worst rating). Here are some examples of what we generated: 

the game is a lot more than a game that is not worth the money to get the game to the point where you have to play the game for a few hours of game play. The game itself is not worth your money on this game. This game is not worth the money to get the game to be a good game. I have to say that this game is not worth the money to get the game to be a good game.

I have to say that this game is the worst game I have ever played. This game is the worst game I have ever played. This game is the worst game I have ever played. This game is the worst game I have ever played. This game is the worst game I have ever played. This game is the worst game I have ever played. This game is the worst game I have ever played. This game is the worst game I have ever played. This game is the worst game I have ever played. This game is the worst game I have ever played. This game is the worst game I have ever played. This game is the worst game I have ever played. This game is the worst game I have ever played. This game is the worst game I have ever played. This game is the worst game I have ever played. This game is the worst game I have ever played. This game is the worst game I have ever played. This game is the worst game I have ever played.

Disclaimer - we clearly did not wait for the network to be fully trained on this one. I do like the idea that someone sat and typed out that last review though. 

We did fully train a network on a weeks worth of livestream chat data (65535 lines). It was maybe not the smartest thing to train on (lots of trash and not politically correct material) - We just have the data mined for another project. You would expect to have seen it generate politically incorrect material.. but it was actually weirdly religious. Here's a verse from it: 

1 Corinthians 15:22 For as in Adam all die, so makes no actually good 


###To Run 
python train.py -data_dir PATH_TO_YOUR_DATA 

And wait! 
After your model is trained get a sample with- 

python sample.py 

To use a beam search to retrieve your sample 

python sample.py --pick 2 --width SOME_WIDTH

