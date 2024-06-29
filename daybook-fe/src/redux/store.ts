import { configureStore } from "@reduxjs/toolkit";
import themeReducer from "./slices/theme";
import drawerReducer from "./slices/drawer";

export const store = configureStore({
  reducer: {
    theme: themeReducer,
    drawer: drawerReducer,
  },
});

// Infer the `RootState` and `AppDispatch` types from the store itself
export type RootState = ReturnType<typeof store.getState>;
// Inferred type: {posts: PostsState, comments: CommentsState, users: UsersState}
export type AppDispatch = typeof store.dispatch;
