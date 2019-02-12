# CM202 Project 2
For this project we are required to set up an RNN and an autoencoder. 

## RNN 
For our RNN we decided to generate video game reviews. To do this, we use hunkim's word level rnn. https://github.com/hunkim/word-rnn-tensorflow

The dataset we chose is 231780 video game reviews from jmcauley's amazon product dataset http://jmcauley.ucsd.edu/data/amazon/. This dataset has some formating errors, so beware that you will need to reformat the json in order to use it as expected. 

Of these reviews there are 14853 1 star reviews (the worst rating). Here are some examples of what we generated: 

`the game is a lot more than a game that is not worth the money to get the game to the point where you have to play the game for a few hours of game play. The game itself is not worth your money on this game. This game is not worth the money to get the game to be a good game. I have to say that this game is not worth the money to get the game to be a good game.`

`I have to say that this game is the worst game I have ever played. This game is the worst game I have ever played. This game is the worst game I have ever played. This game is the worst game I have ever played. This game is the worst game I have ever played. This game is the worst game I have ever played. This game is the worst game I have ever played. This game is the worst game I have ever played. This game is the worst game I have ever played. This game is the worst game I have ever played. This game is the worst game I have ever played. This game is the worst game I have ever played. This game is the worst game I have ever played. This game is the worst game I have ever played. This game is the worst game I have ever played. This game is the worst game I have ever played. This game is the worst game I have ever played. This game is the worst game I have ever played.`

Disclaimer - we clearly did not wait for the network to be fully trained on this one. I do like the idea that someone sat and typed out that last review though. 

We did fully train a network on a weeks worth of livestream chat data (65535 lines). It was maybe not the smartest thing to train on (lots of trash and not politically correct material) - We just have the data mined for another project. You would expect to have seen it generate politically incorrect material.. but it was actually weirdly religious. Here's a verse from it: 

`1 Corinthians 15:22 For as in Adam all die, so makes no actually good `


### To Run 
`python train.py -data_dir PATH_TO_YOUR_DATA `

And wait! 
After your model is trained get a sample with- 

`python sample.py `

To use a beam search to retrieve your sample 

`python sample.py --pick 2 --width SOME_WIDTH`

## Music Autoencoder

Credit to this blog post
https://blog.goodaudience.com/using-tensorflow-autoencoders-with-music-f871a76122ba

Git found here:
https://github.com/wezleysherman/TFMusicAudioEncoder

Download a decent Mp3 or wav data set such as this one
https://zenodo.org/record/1101082#.W5v6BBRlBhE

If you are working with mp3 then they need to be converted. Thankfully there's a handy dandy python def in the process data function. Have a folder named audio and another named audio_wav for this to occur.

Make sure you have all the nessessary dependancy's. Things like pydub and ffmpeg were things I was missing. FFmpeg was something that needed to be manually installed into the contrib folder of your tensorflow enviroment. 

Warning: ffmpeg is buggy and very version sensitive. Depending on your computer enviroment you may need to troubleshoot. Here's a link on how to do that - https://www.tensorflow.org/api_guides/python/contrib.ffmpeg

In python, Import process_data, then run process_data.convert_mp3_to_wav()
 
To run it now:
1. Create a folder named 'output'
2. Put all WAV files for training in the audio_wav folder
3. Open up your terminal within the folder and run python3 encoder.py
4. Pray your computer shines on you with favor.



![IMAGE ALT TEXT HERE](https://scontent-lax3-2.xx.fbcdn.net/v/t1.15752-9/51703042_2121234677913025_624719816590098432_n.jpg?_nc_cat=110&_nc_ht=scontent-lax3-2.xx&oh=c3f3c2558f8445469c1cc4397e00566c&oe=5CDB60BD)



![IMAGE ALT TEXT HERE](https://scontent-lax3-2.xx.fbcdn.net/v/t1.15752-9/52029348_338673123412319_8416514240768114688_n.jpg?_nc_cat=107&_nc_ht=scontent-lax3-2.xx&oh=1fc63001dcc71f65836de3b5ebe6a27c&oe=5CF4AD86)

Blue is the original audio file. Orange is the reconstruction. 
Theses are obviously not very good... Because our run failed...Repeatedly...After many hours of running...Tears were shed....

What you're seeing here is just an NN, not a RNN because unfortunately it is only running through once. 
