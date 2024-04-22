from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Sample past life predictions
past_life_predictions = [
    "In your past life, you were a hermit living in the mountains of Tibet around the year 1500. You spent your days in deep meditation, seeking enlightenment and spiritual truth. Your brief psychological profile: You possessed great wisdom and inner peace, often offering guidance to those who sought it. The lesson that your past life brought to your present incarnation: You are destined to continue your spiritual journey, seeking higher understanding and enlightenment.",
    "You were a sailor in your past life, born in a coastal village in medieval Portugal around the year 1400. Your profession involved exploring distant lands and navigating treacherous seas. Your brief psychological profile: You were adventurous and fearless, with a deep love for the freedom of the open ocean. The lesson that your past life brought to your present incarnation: You are meant to embrace change and adventure, exploring new horizons and experiencing life to its fullest.",
    "In your past life, you were a renowned artist in Renaissance Italy, born in Florence around the year 1450. Your talent and creativity were celebrated throughout the region, and your works still inspire awe today. Your brief psychological profile: You were passionate and driven, with an intense desire to express yourself through your art. The lesson that your past life brought to your present incarnation: You are meant to embrace your creative talents and share them with the world, enriching the lives of others through your work.",
    "You were a scholar in ancient Greece, born in Athens around the year 400 BCE. Your thirst for knowledge was insatiable, and you spent your days studying philosophy, science, and literature. Your brief psychological profile: You were curious and analytical, always seeking to expand your understanding of the world. The lesson that your past life brought to your present incarnation: You are destined to continue your intellectual journey, seeking truth and wisdom wherever it may lead.",
    "In your past life, you were a skilled craftsman in medieval Japan, born in Kyoto around the year 1200. Your talent for woodworking was unmatched, and your creations were admired far and wide. Your brief psychological profile: You were patient and meticulous, taking great pride in your workmanship. The lesson that your past life brought to your present incarnation: You are meant to pursue your passions with dedication and precision, creating beauty and excellence in everything you do.",
    "You were a healer in ancient Egypt, born in Thebes around the year 2000 BCE. Your knowledge of herbs and remedies was legendary, and people traveled from far and wide to seek your aid. Your brief psychological profile: You were compassionate and empathetic, with a deep desire to alleviate the suffering of others. The lesson that your past life brought to your present incarnation: You are meant to use your healing abilities to bring comfort and relief to those in need, nurturing both body and soul.",
    "In your past life, you were a tribal leader in pre-Columbian America, born in the heart of the Amazon rainforest around the year 1000 CE. Your wisdom and leadership skills earned you the respect and admiration of your people. Your brief psychological profile: You were strong and courageous, with a fierce dedication to protecting your community and preserving its traditions. The lesson that your past life brought to your present incarnation: You are meant to lead with integrity and compassion, guiding others towards a brighter future.",
    "You were a nomadic hunter in ancient Mongolia, born on the steppes around the year 800 CE. Your skill with a bow and arrow was unmatched, and you roamed the vast plains in search of game. Your brief psychological profile: You were independent and resourceful, thriving in the freedom of the wilderness. The lesson that your past life brought to your present incarnation: You are meant to embrace your inner strength and adaptability, facing life's challenges with courage and resilience.",
    "In your past life, you were a wise elder in medieval England, born in a small village around the year 1300. Your counsel was sought by all who knew you, and your words were spoken with great authority. Your brief psychological profile: You were wise and compassionate, with a deep understanding of human nature. The lesson that your past life brought to your present incarnation: You are meant to share your wisdom and guidance with others, offering insight and support on their journey through life.",
    "You were a revolutionary in ancient Rome, born in the city of Pompeii around the year 50 CE. Your passion for justice and equality led you to challenge the oppressive regime of the ruling elite. Your brief psychological profile: You were bold and fearless, willing to risk everything for the cause you believed in. The lesson that your past life brought to your present incarnation: You are meant to stand up for what is right and fight against injustice, using your voice to create positive change in the world.",
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        day = request.form['day']
        month = request.form['month']
        year = request.form['year']

        # Perform some logic to predict past life (random for demonstration)
        prediction = random.choice(past_life_predictions)

        return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
