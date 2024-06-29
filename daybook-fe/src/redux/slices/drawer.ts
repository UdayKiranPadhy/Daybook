import { createSlice } from "@reduxjs/toolkit";

export interface DrawerState {
  value: boolean;
}

const initialState: DrawerState = {
  value: true,
} satisfies DrawerState as DrawerState;

export const drawerSlice = createSlice({
  name: "drawer",
  initialState,
  reducers: {
    toggleDrawer: (state: DrawerState) => {
      state.value = !state.value;
    },
  },
});

// Action creators are generated for each case reducer function
export const { toggleDrawer } = drawerSlice.actions;

export default drawerSlice.reducer;
