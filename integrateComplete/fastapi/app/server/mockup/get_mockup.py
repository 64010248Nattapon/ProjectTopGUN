# import requests
# import json
# from fastapi import APIRouter

# from server.models.water import (
#     ErrorResponseModel,
#     ResponseModel,
#     UpdateWaterModel,
# )

# from server.database import (
#     add_water,
#     delete_water,
#     retrieve_water,
#     retrieve_waters,
#     update_water,
# )

# router = APIRouter()


# @router.get("/{id}", response_description="water data retrieved")
# async def get_mockup_data(id):
#     # url = 'http://192.168.10.159/v1/'+str(id)
#     # url = 'https://jsonplaceholder.typicode.com/albums'#/'+str(id)
#     url = "http://10.66.6.97:80/"+str(id)  # /'+str(id)
#     mockup = requests.get(url)
#     if mockup:
#         mesage = mockup.json()
#         mesage = mesage[0]
#         time = mesage["w_date"].split("T")[0].split("-")
#         Object: UpdateWaterModel = {
#             # "Name":"",
#             # "Year": time[0],
#             "Date": time["Date"],
#             # "Month": time[2],
#             "w_height": mesage["w_height"],
#             "w_discharge": mesage["w_discharge"],
#             # "WaterDrainRate": mesage["WaterDrainRate"],
#         }
#         # print(json.loads(mockup.text))
#         # return ResponseModel(str(mockup.text), "API data id:" +str(id) +" retrieved successfully")
#         return mesage
#         # return await add_water(Object),ResponseModel(str(mockup.text),"API data id:" + str(id)+"retrieved successfully")

#     return ErrorResponseModel("An error occurred.", 404, "data doesn't exist.")


# # @router.post("/{id}", response="Save to DB")
# # async def add_data(message: UpdateWaterModel):
# #     # Insert the received data into the MongoDB collection
# #     collection.insert_one({
# #         "w_date": message.w_date,
# #         "w_height": message.w_height,
# #         "w_cubic": message.w_cubic
# #     })

# #     return ResponseModel("Data saved to DB successfully", "Data saved successfully")
