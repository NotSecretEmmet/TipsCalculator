from django import forms

class UploadFileForm(forms.Form):
    Dyflexis_excel_export = forms.FileField(
        label= "Dylfexis Excel export",
    	help_text='Select the Gepland/Gewerkt lijst export Excel file downloaded from Dylfexis.')
    check_isoweek = forms.BooleanField(
    	required=False, 
    	help_text='Check to ensure that all dates are within a given isoweek.')
    tips_amount = forms.IntegerField(
    	help_text='Enter the total amount of tips to be distributed among the employees based upon hours worked in a given department.')
    overtips_amount = forms.IntegerField(
    	help_text='Enter the amount of tips to be reallocated to the overtips from the total amount above.')
