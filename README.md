# ML-Smart-Home-Assistant

![ASK_overview _TTH_](https://user-images.githubusercontent.com/67477345/143164667-786523bc-9b76-4d32-b2ba-a5c16055f9ab.png)

## Pipeline

#### Automatic Speech Recognition -> Natural Language Understanding -> Dialogue System -> Text To Speech

![](https://opendatascience.com/wp-content/uploads/2021/03/nlp2-1.png)

#### ASR
Automatic speech recognition (ASR) is technology that converts spoken words into text.

![](https://miro.medium.com/max/1400/1*yP_TSDUBmjEh0broCh0wYg.png)

#### NLU
Natural-language understanding (NLU) is a subtopic of natural-language processing. With natural language understanding (NLU), computers can deduce what a speaker actually means, and not just the words they say.

![](https://d3ogm7ac91k97u.cloudfront.net/content/dam/alexa/temp-working-folder/nlu/nlu-lp_graphics_block-1._CB499232483_.png)

To begin, we will need to understand the basics of NLU.

**Utterances**

The utterances are spoken or typed phrases that users input to NLU for fulfiling the intent. Simply speaking, this is how the users express their intent in words. Examples could be “Can I book a ticket from Seattle to Beijing?” or “I would like to buy a ticket for Septempber 19”. For NLU to classify intents based on utterances, a model needs to be trained with pre-defined utterance examples.

**Intents**

Intents are response to the natural-language input from the users. For example, in an airline booking application. Intents can be Book Tickets, Cancel Tickets or View Ticket Details. When the user input comes in, the NLU needs to classify to find an appropriate (mostly likely matched) intent. This relies on training a model based on utterances.

**Slots or Entities**

Slots are variables in the utterance which is required to fulfil the intent. For example, when booking an airline ticket, the variables could be the departure date, return date, destination, departure city.

