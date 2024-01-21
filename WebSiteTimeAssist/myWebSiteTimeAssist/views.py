# Create your views here.

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
import firebase_admin
from firebase_admin import firestore, auth

import logging

logger = logging.getLogger(__name__)

@login_required
def delete_account(request):
    logger.info("START")
    user = request.user

    # Delete data from Firebase Firestore
    db = firestore.client()
    user_uid = str(user.id)
    logger.info("USER_UID %s", user_uid)

    if False:
        # delete users collection documents
        user_ref_list = db.collection('users').where("uid", "==", user_uid).get()
        for user_ref in user_ref_list:
            user_ref.delete()

            # delete users collection documents
        categories_ref_list = db.collection('categories').where("uid", "==", user_uid).get()
        for user_category_ref in categories_ref_list:
            user_category_ref.delete()

        # delete users collection documents
        tasks_ref_list = db.collection('tasks').where("uid", "==", user_uid).get()
        for user_tasks_ref in tasks_ref_list:
            user_tasks_ref.delete()

        # delete users collection documents
        weeklyTable_ref_list = db.collection('weeklyTable').where("uid", "==", user_uid).get()
        for user_weeklyTable_ref in weeklyTable_ref_list:
            user_weeklyTable_ref.delete()


        # delete users collection documents
        weeklyTableIDs_ref_list = db.collection('weeklyTableIDs').where("uid", "==", user_uid).get()
        for user_weeklyTableIDs_ref in weeklyTableIDs_ref_list:
            user_weeklyTableIDs_ref.delete()

        
        # delete users collection documents
        workingDaysSchedule_ref_list = db.collection('workingDaysSchedule').where("uid", "==", user_uid).get()
        for user_workingDaysSchedule_ref in workingDaysSchedule_ref_list:
            user_workingDaysSchedule_ref.delete()

        # delete users collection documents
        workingDaysScheduleID_ref_list = db.collection('workingDaysScheduleID').where("uid", "==", user_uid).get()
        for user_workingDaysScheduleID_ref in workingDaysScheduleID_ref_list:
            user_workingDaysScheduleID_ref.delete()

        # Delete Firebase Auth user
        auth.delete_user(user_uid)

        # Delete Django user account
        user.delete()

    return redirect('/')


def user_profile(request):
    return render(request, 'user_profile.html')

def delete_account_rendering(request):
    return render(request, 'delete_account.html')

def home_rendering(request):
    return render(request, 'base.html')