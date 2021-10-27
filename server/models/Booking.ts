import { Schema, model } from "mongoose";

interface Booking {
  userId: string;
  name: string;
  genre: string | null;
  phone: string;
  email: string | null;
  nationality: string | null;
  peopleQty: number;
  currentDebt: number;
  placeName: string;
  totalCost: number;
  payment: number;
}

const BookingSchema = new Schema<Booking>({
  userId: { type: String, required: true },
  name: { type: String, default: "Juanito Alimaña" },
  genre: { type: String, default: null },
  phone: { type: String, default: "0000-0000" },
  email: { type: String, default: null },
  nationality: { type: String, default: null },
  peopleQty: { type: Number, default: 1 },
  currentDebt: { type: Number, default: 0 },
  placeName: { type: String, required: true },
  totalCost: { type: Number, required: true },
  payment: { type: Number, default: 0 },
});

const BookingModel = model<Booking>("bookings", BookingSchema);

export default BookingModel;

export { Booking };
