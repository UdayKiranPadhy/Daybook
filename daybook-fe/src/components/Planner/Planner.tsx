import React, { useCallback, useEffect, useRef, useState } from "react";
import "./Planner.css";
import { sampleData } from "../../utils/sample";
import axios from "axios";

// will use query for date adjustment
type DataType = {
  title: string;
  ia_collection_s: string;
};
function Planner({ drawerOpen }: { drawerOpen: any }) {
  const pageNo = useRef(1);
  const [currentData, setCurrentData] = useState<DataType[]>([]);
  const [loading, setLoading] = useState(false);
  const [query, setQuery] = useState("spy");
  const ENDPOINT = (pageNo: Number, query: string) =>
    `https://openlibrary.org/search.json?q=${query}&page=${pageNo}&limit=7`;
  useEffect(() => {
    fetchData(pageNo.current, query);
  }, [query]);
  const observer: any = useRef(null);
  const lastElementObserver = useCallback(
    (node: any) => {
      if (loading) return;
      if (observer.current) observer.current.disconnect();
      observer.current = new IntersectionObserver((entries) => {
        if (entries[0].isIntersecting) {
          pageNo.current += 1;
          fetchData(pageNo.current, query);
        }
      });
      if (node) observer.current.observe(node);
    },
    [query]
  );

  const fetchData = useCallback(
    (pageNo: Number, query: string) => {
      setLoading(true);
      axios
        .get(ENDPOINT(pageNo, query))
        .then((res: any) => {
          const data = res.data;
          const { docs = [] } = data;
          console.log(docs);

          setCurrentData((value) => [...value, ...docs]);
        })
        .catch((err: any) => console.log(err))
        .finally(() => setLoading(false));
    },
    [query]
  );
  const dataRendering = (arrayOfData: any) => {
    return arrayOfData?.map((data: any, index: number) => {
      if (index === arrayOfData.length - 1) {
        return renderItem(data, index, lastElementObserver);
      }
      return renderItem(data, index, null);
    });
  };
  const renderItem = (item: any, index: any, ref: any) => {
    const { title } = item;
    const description =
      "Looking back on a childhood filled with events and memories, I find it rather difficult to pick on that leaves me with the fabled “warm and fuzzy feelings.” As the daughter of an Air Force Major, I had the pleasure of traveling across America in many moving trips. I have visited the monstrous trees of the Sequoia National Forest, stood on the edge of the Grande Canyon and have jumped on the beds at Caesar’s Palace in Lake Tahoe. However, I have discovered that when reflecting on my childhood, it is not the trips that come to mind, instead there are details from everyday doings; a deck of cards, a silver bank or an ice cream flavor. One memory that comes to mind belongs to a day of no particular importance. It was late in the fall in Merced, California on the playground of my old elementary school; an overcast day with the wind blowing strong. I stood on the blacktop, pulling my hoodie over my ears. The wind was causing miniature tornados; we called them “dirt devils”, to swarm around me.";
    return (
      <article ref={ref} key={index} className="planner-item primary-container">
        <h5>{title}</h5>
        <p>{description}</p>
      </article>
    );
  };
  return (
    <>
      <div className={`planner-container ${drawerOpen ? "draweropen" : ""}`}>
        {dataRendering(currentData)}
      </div>
    </>
  );
}

export default Planner;
