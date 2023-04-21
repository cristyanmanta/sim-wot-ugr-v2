import firebase_admin
import heapq
import logging
import math
import random
import threading
import time

from datetime import datetime
from firebase_admin import credentials
from firebase_admin import firestore
from flask import Flask, render_template, request, jsonify
from model_virtual_thing import create_random_virtual_thing
from scipy.stats import poisson


# Initialising Logs
format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
logging.info(" > Main    : Loading App ... ")

# Initialising the FireBase Client for continuously getting the state variables
logging.info(" > Main    : Initializing Firebase connection...")
firebase_credential = credentials.Certificate('ir-wot-ugr-credential.json')
firebase_app = firebase_admin.initialize_app(firebase_credential)

# Getting access to Firebase instance
firebase_db = firestore.client()
logging.info(" > Main    : Firebase connection initialised")

# Instantiating Flask App
app = Flask(__name__, static_url_path='/static')


# --------------------------------------------------------------------------------------------------------------------


def sim_write_entity(vCreatedEntity):
    title = ''
    title = 'VTH' + title.ljust(7 - int(math.log10(vCreatedEntity['id'])), '0')
    # --> Point to new "IRTestCollection'
    firebase_db.collection('IRTestCollection').document(title+str(vCreatedEntity['id'])).set(vCreatedEntity)
    return


def sim_delete_simulation():
    documents = firebase_db.collection('documents').stream()    # --> Point to new "IRTestCollection'
    for doc in documents:
        doc.reference.delete()
    changes = firebase_db.collection('crawlerPipe').stream()
    for change in changes:
        change.reference.delete()
    return


def sim_write_stats(sim_stats_id, simCycles, simEntities, simIntelligentZones, simSmartSpaces, simSmartSubSpaces, simVirtualThings, simVirtualSensors):
    firebase_db.collection('statsSIMWoT').document(sim_stats_id).set(
        {
            'simCycles': simCycles,
            'simEntities': simEntities,
            'simIntelligentZones': simIntelligentZones,
            'simSmartSpaces': simSmartSpaces,
            'simSmartSubSpaces': simSmartSubSpaces,
            'simVirtualThings': simVirtualThings,
            'simVirtualSensors': simVirtualSensors
            # 'simTimeStamp': '2023'
        }
    )
    return


def thread_function(sim_entities):
    logging.info(" > Thread %s: starting", sim_entities)
    vCreatedEntity = create_random_virtual_thing(sim_entities)
    sim_write_entity(vCreatedEntity)
    # print(vCreatedEntity)
    # time.sleep(2)
    logging.info(" > Thread %s: finishing", sim_entities)


# def sim_wot_function_v2(max_entities, max_time):
if __name__ == "__main__":

    # Experiment Set #1
    # Setting up the number of vThings to be created  sim_wot_function_v2(max_entities, max_time)
    logging.info(" > Main    : Before creating threads")
    max_entities = 5
    max_time = 1000
    # logging.info(" > Main    : Before running threads")
    # x.start()
    # logging.info(" > Main    : Wait for the thread to finish")
    # x.join()
    # logging.info(" > Main    : All done")

    global id
    logging.info(" > Thread Simulation Engine: Waiting ... ")

    # Reinitialise the Simulation
    logging.info(" > Thread Simulation Engine: Cleaning ... ")
    sim_delete_simulation()

    # "Simulation starting..."
    logging.info(" > Thread Simulation Engine: Simulation starting ... ")
    id = datetime.now()
    ids = []
    mu = 1
    sim_cycles = 0
    sim_time = 0
    sim_entities = 0
    actual_action = {}
    actual_action[1] = None

    # Event-Driven Mechanism built upon a Heap
    heap = []

    # Creation of first event in Heap at random time following Poisson Distribution.
    heapq.heappush(heap, (poisson.rvs(mu, size=1)[0], 'thing_creation'))
    heapq.heappush(heap, (poisson.rvs(mu, size=1)[0], 'thing_creation'))
    heapq.heappush(heap, (poisson.rvs(10 * mu, size=1)[0], 'thing_movement'))
    limit_time = max_time
    limit_entities = max_entities

    sim_events = 0
    start_time = time.time()

    # Loop for executing the WoT Simulation.
    while sim_time < limit_time:
        # Print Current Conditions
        # print("        :  --->  Imminent Event is:    " + str(actual_action[1]))
        # print("        :  --->  Current Sim Cycles:   " + str(sim_cycles))
        # print("        :  --->  Current Sim Events:   " + str(sim_events))
        # print("        :  --->  Current Sim Time is:  " + str(sim_time))
        # print("        :  --->  Current Sim Entities: " + str(sim_entities))

        # Report Simulation Stats
        # sim_write_stats('sim_stats_now', int(sim_cycles), int(limit_entities), 1, 1, 421, int(sim_entities)-1, int(sim_entities)-1)

        # Extract next event from the Heap
        actual_action = heapq.heappop(heap)
        sim_time = actual_action[0]
        sim_cycles += 1
        sim_events += 1

        # Creation of last Event in the Engine before End of Simulation
        if sim_entities == limit_entities:
            sim_entities += 1
            heapq.heappush(heap, (sim_time + poisson.rvs(mu, size=1)[0], 'thing_disconnection'))
        elif sim_entities == limit_entities + 1:
            # sim_write_experiments(task_simulator_state['index-structure'])
            break

        if actual_action[1] == 'thing_creation' and sim_entities < limit_entities:
            sim_entities += 1

            # Create vThing # X Create vSensor
            x = threading.Thread(target=thread_function, args=(sim_entities,))
            if sim_entities % 100 == 0:
                None
                # time.sleep(2)
            else:
                x.start()
            # vCreatedEntity = create_random_virtual_thing(sim_entities)
            # Store in FireBase the vThings
            # sim_write_entity(vCreatedEntity)
            # title = ''
            # title = 'VTH' + title.ljust(7 - int(math.log10(vCreatedEntity['name'])), '0') + str(sim_entities)
            # ids.append(title)

            heapq.heappush(heap, (sim_time + poisson.rvs(mu, size=1)[0], 'thing_creation'))

        # Adding other events to the Simulation Heap.
        elif actual_action[1] == 'thing_disconnection':
            # Disconnect_thing(key)
            heapq.heappush(heap, (sim_time + poisson.rvs(mu, size=1)[0], 'thing_creation'))
            heapq.heappush(heap, (sim_time + poisson.rvs(mu, size=1)[0], 'thing_disconnection'))
            if sim_entities > limit_entities and len(ids) > 0:
                # id_to_remove = random.choice(ids)
                # ids.remove(id_to_remove)
                None
        #
    end_time = time.time()
    delta_time = end_time - start_time
    entity_time = max_entities/delta_time
    logging.info(" > Thread Simulation Engine: Simulation stopped X ")
    logging.info(" > Simulation Time (Secs): " + str(delta_time))
    logging.info(" > Simulation Speed (vThings/Sec): " + str(entity_time))

    # return
