from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired
from data import specializations
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# نموذج اختيار تخصص من القائمة
class SpecializationForm(FlaskForm):
    specialization = SelectField('Choose your specialization:', choices=[], validators=[DataRequired()])
    submit = SubmitField('Show Details')

# أسئلة اختبار traits + ربطهم بالسمات personality traits لكل سؤال
quiz_questions_ar = {
    "q1": "هل تفضل التفكير المنطقي وحل المشكلات المعقدة؟",
    "q2": "هل أنت شخص حذر وتنتبه للتفاصيل الصغيرة؟",
    "q3": "هل تحب العمل ضمن فريق والتخطيط المسبق؟",
    "q4": "هل تمتلك فضولاً وابتكاراً لحل الأمور بطرق جديدة؟",
    "q5": "هل تفضل العمل اليدوي والتعامل المباشر مع الأجهزة والتقنيات؟",
    "q6": "هل أنت منظم وتهتم بالجوانب التجارية والعملية؟",
    "q7": "هل أنت مبدع وتحب التفكير خارج الصندوق؟",
    "q8": "هل تولي اهتماماً كبيراً للدقة والتفاصيل؟",
    "q9": "هل تمتلك مهارات تحليلية واستراتيجية؟",
    "q10": "هل تفضل العمل بشكل مستقل وذاتي؟"
}

quiz_traits_map = {
    "q1": ["logical", "analytical"],
    "q2": ["cautious", "observant"],
    "q3": ["team_player", "planner"],
    "q4": ["innovative", "curious"],
    "q5": ["technical", "hands_on"],
    "q6": ["organizational", "business_minded"],
    "q7": ["creative", "planner"],
    "q8": ["detail_oriented", "technical"],
    "q9": ["analytical", "strategic"],
    "q10": ["independent", "curious"]
}

@app.route('/', methods=['GET', 'POST'])
def index():
    form = SpecializationForm()
    form.specialization.choices = [(key, key) for key in specializations.keys()]
    if form.validate_on_submit():
        return redirect(url_for('result', spec_name=form.specialization.data))
    return render_template('index.html', form=form)

@app.route('/result/<spec_name>')
def result(spec_name):
    details = specializations.get(spec_name)
    if not details:
        flash("Sorry, that specialization does not exist.")
        return redirect(url_for('index'))
    return render_template('result.html', spec_name=spec_name, details=details)

@app.route('/quiz/ar', methods=['GET', 'POST'])
def quiz_ar():
    if request.method == 'POST':
        answers = request.form
        trait_scores = {}

        for q, traits in quiz_traits_map.items():
            if answers.get(q) in ["yes", "ممكن"]:  # ← تعديل للإجابة "ممكن"
                for trait in traits:
                    trait_scores[trait] = trait_scores.get(trait, 0) + 1

        spec_scores = {}
        for spec, data in specializations.items():
            score = 0
            for trait in data.get("traits", []):
                score += trait_scores.get(trait, 0)
            spec_scores[spec] = score

        sorted_specs = sorted(spec_scores.items(), key=lambda x: x[1], reverse=True)
        best_specs = [spec for spec, score in sorted_specs if score > 0][:3]

        return render_template('quiz_result.html', best_specs=best_specs, specialization_data=specializations)

    return render_template('quiz.html', questions=quiz_questions_ar)

# ✅ الجزء الأهم: لازم يكون موجود لتشغيل السيرفر
if __name__ == '__main__':
    print("🚀 Flask is running... Visit http://127.0.0.1:5000")
    app.run(debug=True)
