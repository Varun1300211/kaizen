from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectMultipleField, widgets, FileField
from wtforms.validators import DataRequired

class MyForm(FlaskForm):
    # Example: Checkbox field for colors
    colors = SelectMultipleField(
        'Colors',
        option_widget=widgets.CheckboxInput(),
        widget=widgets.ListWidget(prefix_label=True)
    )

class LoginForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    employee_code = StringField('Employee Code', validators=[DataRequired()])
    area = StringField('Plant/Area', validators=[DataRequired()])
    mobile = StringField('Mobile No.', validators=[DataRequired()])
    impact = SelectMultipleField('Impact Area', option_widget=widgets.CheckboxInput(), widget=widgets.ListWidget(prefix_label=True), validators=[DataRequired()])
    before_date = StringField('Before Status Date', validators=[DataRequired()])
    before_image = FileField('Before Status Image', validators=[DataRequired()])
    after_date = StringField('After Status Date', validators=[DataRequired()])
    after_image = FileField('After Status Image', validators=[DataRequired()])
    problem = StringField('Problem Present Before', validators=[DataRequired()])
    action = StringField('Action you took to correct it', validators=[DataRequired()])
    benefits = StringField('Benefits for the change', validators=[DataRequired()])
    submit = SubmitField('Submit')