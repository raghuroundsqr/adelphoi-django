import axios from "axios";
import * as Types from "./definitions";

const baseApiUrl = "http://13.232.1.126:8000/first_match";

interface PredictionResponse {
  referred_program: string;
  model_program: string;
}

interface LocationsResponse {
  "Suggested Locations": string[];
}

export const updateConfiguration = async (
  configuration: Types.Configuration
) => {
  try {
    const response = await axios.post(`${baseApiUrl}/save`, configuration);

    console.log("inserted new configuration. the configuration is ");
    console.log(response);
    const r = {
      ...response.data,
      program_type: response.data.program_type[0]
    };
    return (r as unknown) as Partial<Types.Configuration>;
  } catch (error) {
    console.error("api function insertClient error");
    // console.log(error);
    throwError(error);
  }
};

export const insertClient = async (client: Types.Client) => {
  try {
    const response = await axios.post(`${baseApiUrl}/list_view/`, client);

    console.log("inserted new client. the client is ");
    console.log(response);
    const r = {
      ...response.data,
      program_type: response.data.program_type[0]
    };
    return (r as unknown) as Partial<Types.Client>;
  } catch (error) {
    console.error("api function insertClient error");
    // console.log(error);
    throwError(error);
  }
};

export const insertPrediction = async (client: Types.Client) => {
  try {
    const response = await axios.get(
      `${baseApiUrl}/result/${client.client_code}`
    );
    const data = (response.data as unknown) as PredictionResponse;
    const newCl = {
      ...client,
      referred_program: data["referred_program"],
      model_program: data["model_program"]
    };
    console.log("inserted new prediction. the client is ");
    console.log(newCl);
    return newCl;
  } catch (error) {
    console.error("api function insertPrediction error");
    throwError(error);
  }
};

export const fetchLocations = async (
  client_code: string,
  selected_program: string
) => {
  try {
    const response = await axios.get(
      `${baseApiUrl}/location/${client_code}?client_selected_program=${selected_program}`
    );
    const data = (response.data as unknown) as LocationsResponse;
    console.log("received locations from server ", data);
    return data["Suggested Locations"];
  } catch (error) {
    console.error("api function getLocations error");
    throwError(error);
  }
};

export const saveLocationAndProgram = async (
  client_code: string,
  selected_program: string,
  selected_location: string
) => {
  try {
    const response = await axios.put(
      `${baseApiUrl}/update_list/${client_code}/`,
      {
        client_selected_program: selected_program,
        client_selected_locations: selected_location
      }
    );
    console.log(response);
    return response.data;
  } catch (error) {
    console.error("api function getLocations error");
    throwError(error);
  }
};

export const updateProgramCompletion = async (
  client_code: string,
  Program_Completion: string,
  Returned_to_Care: string
) => {
  try {
    const response = await axios.put(
      `${baseApiUrl}/program_complete/${client_code}/`,
      {
        Program_Completion,
        Returned_to_Care
      }
    );
    console.log(response);
    return response.data.data;
  } catch (error) {
    console.error("api function getLocations error");
    throwError(error);
  }
};

export const searchClient = async (
  client_code: string,
  client_name: string
) => {
  try {
    const response = await axios.get(
      `${baseApiUrl}/search/?name=${client_name}&client_code=${client_code}`
    );
    console.log(response);
    return response.data;
  } catch (error) {
    console.error("api function searchClient error");
    throwError(error);
  }
};

function throwError(error: any) {
  if (error.response) {
    // The request was made and the server responded with a status code
    // that falls out of the range of 2xx
    console.log(error.response.data);
    console.log(error.response.status);
    console.log(error.response.headers);
    const errorResponse = {
      data: error.response.data || undefined,
      status: error.response.status || undefined
    };
    throw errorResponse;
  } else if (error.request) {
    // The request was made but no response was received
    // `error.request` is an instance of XMLHttpRequest in the browser and an instance of
    // http.ClientRequest in node.js
    console.log(error.request);
    const errorResponse = {
      data: { Error: "unknown error occurred while contacting the server" },
      status: undefined
    };
    throw errorResponse;
  } else {
    // Something happened in setting up the request that triggered an Error
    console.log("Error", error.message);
  }
}
