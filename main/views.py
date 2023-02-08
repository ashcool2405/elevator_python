import json
from django.http import JsonResponse
from rest_framework.views import APIView
from .elevatorsystem.main import ElevatorSystem


class ElevatorNumber(APIView):

    def post(self, request):
        try:
            no_of_lifts = request.data['number_of_lift']
            request.session['number_of_lift'] = no_of_lifts
            intial_positions = request.data['intial_position']
            request.session['intial_positions'] = intial_positions
            print(no_of_lifts, intial_positions)
            return JsonResponse({"response": True}, status=200)
        except Exception as e:
            print(e)
            return JsonResponse({"response": False}, status=400)


class Floor(APIView):

    def post(self, request):
        try:
            min_floor = request.data['min_floor']
            request.session['min_floor'] = min_floor
            max_floor = request.data['max_floor']
            request.session['max_floor'] = max_floor
            active_floor = request.data['active_floor']
            request.session['active_floor'] = active_floor
            return JsonResponse({"response": True}, status=200)
        except Exception as e:
            print(e)
            return JsonResponse({"response": False}, status=400)


class ReqOfElevator(APIView):

    def post(self, request):
        try:
            req_matrix = request.data['req_raised']
            request.session['req_raised'] = req_matrix
            return JsonResponse({"response": True}, status=200)
        except Exception as e:
            print(e)
            return JsonResponse({"response": False}, status=400)


class LiftHistory(APIView):

    def get(self, request):
        try:
            lift_number = request.query_params['lift_number']
            no_of_lifts = request.session.get('number_of_lift')
            floor_min = request.session.get('min_floor')
            floor_max = request.session.get('max_floor')
            request_each = request.session.get('req_raised')
            lift_positions = request.session.get('intial_position')
            active_floor = request.session.get('active_floor')
            elevator_sys = ElevatorSystem(no_of_lifts, floor_min, floor_max, request_each, lift_positions)
            return JsonResponse({"response": json.dump(elevator_sys.process_request(active_floor, lift_number))}, status=200)
        except Exception as e:
            print(e)
            return JsonResponse({"response": False}, status=400)



