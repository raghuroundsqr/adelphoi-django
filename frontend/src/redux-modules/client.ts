import { ThunkAction } from "redux-thunk";
import { AnyAction } from "redux";
// import { createSelector } from 'reselect';

import createReducer from "./createReducer";
import { ClientState } from "./definitions/State";
import { AppState } from "../redux-modules/root";
import * as Types from "../api/definitions";
import {
  insertClient,
  insertPrediction,
  fetchLocations,
  saveLocationAndProgram,
  searchClient,
  updateProgramCompletion
} from "../api/api";

const initialState: ClientState = {
  client: Types.emptyClient,
  clientList: {},
  errors: {},
  excludePage2: false,
  page1FormCompleted: false,
  page2FormCompleted: false
};
// TODO handle negative cases
// 1. new client creation fails - with and without excl.
// 2. submit prediction responds with error - no program found.
// 3. get locations responds with error - no locations found or empty array.

const { reducer, update } = createReducer<ClientState>(
  "Client/UPDATE",
  initialState
);
export const clientReducer = reducer;

export const actions = {
  update,

  updateProgramCompletion(
    client_code: string,
    Program_Completion: number,
    Returned_to_Care: number
  ): ThunkAction<Promise<string>, AppState, null, AnyAction> {
    return async (dispatch, getState) => {
      const response = await updateProgramCompletion(
        client_code,
        Program_Completion,
        Returned_to_Care
      );
      if (!response) {
        throw Error("something went wrong while submitting");
      }
      // return (response as unknown) as string;
      const clientState = getState().client;
      const clientList = clientState ? clientState.clientList : {};
      if (Object.keys(clientList).length > 0) {
        const cl = clientList[client_code];
        if (!cl) {
          return (response as unknown) as string;
        }
        const updatedCl = {
          ...cl,
          Program_Completion,
          Returned_to_Care
        };
        if (!updatedCl.client_code) {
          return (response as unknown) as string;
        }
        const updatedClList = {
          ...clientList,
          [updatedCl.client_code]: updatedCl
        };
        dispatch(update({ clientList: updatedClList }));
      }
      // dispatch(update({ client: clresult }));
      return (response as unknown) as string;
    };
  },

  getLocations(
    client_code: string,
    selected_program: string
  ): ThunkAction<Promise<Types.Client | undefined>, AppState, null, AnyAction> {
    return async (dispatch, getState) => {
      const response = await fetchLocations(client_code, selected_program);
      const locations = response ? response["Suggested Locations"] : [];
      if (locations.length > 0) {
        const cl: Types.Client = {
          ...getState().client!.client,
          SuggestedLocations: [...locations],
          client_selected_program: selected_program
        };
        dispatch(update({ client: cl }));
        return cl;
      }
    };
  },

  saveLocationAndProgram(
    selected_location: string
  ): ThunkAction<Promise<Types.Client | undefined>, AppState, null, AnyAction> {
    return async (dispatch, getState) => {
      const client = getState().client!.client;
      const cl: Types.Client = {
        ...client,
        client_selected_locations: selected_location
      };
      dispatch(update({ client: cl }));

      const response = await saveLocationAndProgram(
        client.client_code!,
        client.client_selected_program!,
        selected_location
      );
      if (!response) {
        throw Error("something went wrong while submitting");
      }
      const clresult: Types.Client = {
        ...cl,
        result_final: response.result
      };
      dispatch(update({ client: clresult }));
      return clresult;
    };
  },

  submitPrediction(
    client: Types.Client
  ): ThunkAction<Promise<Types.Client | undefined>, AppState, null, AnyAction> {
    return async (dispatch, getState) => {
      let locations: string[] = [];

      if (!client.client_code) {
        throw new Error("client code required");
      }
      dispatch(update({ client }));
      try {
        const response = await insertPrediction(client);
      } catch (error) {
        throw error;
      }
      try {
        const response = await fetchLocations(
          client.client_code,
          client.program_type!
        );
        if (response && response["result"] && response["result"] !== "") {
          throw new Error(response["result"]);
        }
        if (response && response["Suggested Locations"]) {
          locations = response["Suggested Locations"];
        }
        if (locations.length > 0) {
          const cl: Types.Client = {
            ...client,
            SuggestedLocations: [...locations],
            client_selected_program: client.program_type
          };
          dispatch(update({ client: cl }));
          return cl;
        }
      } catch (error) {
        throw error;
      }
    };
  },

  insertClient(
    client: Types.Client
  ): ThunkAction<Promise<Types.Client | undefined>, AppState, null, AnyAction> {
    return async (dispatch, getState) => {
      try {
        const response = await insertClient(client);
        if (!response) {
          throw Error("something went wrong while saving the client");
        }

        if (response["Result"] && response["Result"].trim() !== "") {
          return client;
        }

        const cl = {
          ...client,
          program_type: response.program_type || null,
          Confidence: response.Confidence || null,
          referred_program: response.referred_program || null,
          model_program: response.model_program || null
        };
        dispatch(update({ client: cl }));
        return cl;
      } catch (errors) {
        dispatch(update({ client, errors: errors }));
        throw errors;
      }
    };
  },

  searchClient(
    client_code: string,
    client_name: string
  ): ThunkAction<Promise<void>, AppState, null, AnyAction> {
    return async (dispatch, getState) => {
      const response = await searchClient(client_code, client_name);
      let clientList: { [key: string]: Types.Client } = {};
      response.map((c: Types.Client) => {
        if (c.client_code) {
          return (clientList[c.client_code] = c);
        }
      });
      dispatch(update({ clientList }));
    };
  },

  upsertClient: (
    client: Types.Client,
    page1FormCompleted: boolean = false,
    excludePage2: boolean = false
  ): ThunkAction<void, AppState, void, any> => {
    const newCl = {
      ...client,
      primaryRaceCode: "1",
      ageAtEpisodeStart: "1",
      ageAtEnrollStart: "1",
      english_second_lang: "1",
      enrollStart_date: null,
      type_of_drugs: "aaa",
      FAST_FamilyTogetherScore: "0",
      FAST_CaregiverAdvocacyScore: "0"
    };
    return (dispatch, getState) => {
      dispatch(update({ client: newCl, page1FormCompleted, excludePage2 }));
    };
  },

  clear(): ThunkAction<Promise<void>, AppState, null, AnyAction> {
    return async dispatch => {
      dispatch(
        update({
          client: Types.emptyClient,
          page1FormCompleted: false,
          excludePage2: false
        })
      );
    };
  },

  clearErrors(): ThunkAction<Promise<void>, AppState, null, AnyAction> {
    return async dispatch => {
      dispatch(update({ errors: {} }));
    };
  }
};

export const selectors = {
  //
};
