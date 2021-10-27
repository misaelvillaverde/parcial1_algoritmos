import { Schema, model } from "mongoose";

interface TuristicPlace {
  name: string;
  image?: string;
  description: string;
  includes: string[];
  cost: number;
}

interface Province {
  name: string;
  image?: string;
  description: string;
  indigenousRegion: boolean;
  turisticPlaces: TuristicPlace[];
}

const TuristicPlaceSchema = new Schema<TuristicPlace>({
  name: { type: String, required: true },
  image: { type: String, default: null },
  description: { type: String, required: true },
  includes: { type: [String], required: true },
  cost: { type: Number, required: true },
});

const ProvinceSchema = new Schema<Province>({
  name: { type: String, required: true },
  image: { type: String, default: null },
  description: { type: String, required: true },
  indigenousRegion: { type: Boolean, required: true },
  turisticPlaces: [TuristicPlaceSchema],
});

const ProvinceModel = model<Province>("province", ProvinceSchema);

export default ProvinceModel;
