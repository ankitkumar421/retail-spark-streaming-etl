{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "4695fc20-7803-47be-b078-88e832cd5b78",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Columns: Index(['YEAR', 'MONTH', 'SUPPLIER', 'ITEM CODE', 'ITEM DESCRIPTION',\n",
      "       'ITEM TYPE', 'RETAIL SALES', 'RETAIL TRANSFERS', 'WAREHOUSE SALES'],\n",
      "      dtype='object')\n",
      "Wrote: data/streaming_input/sales_1970-01-01.csv (307645 records)\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import os\n",
    "\n",
    "# Path to your downloaded sales data\n",
    "sales_file = 'data/Sales.csv'\n",
    "\n",
    "# Where to output split files (must exist, or will be created)\n",
    "stream_dir = 'data/streaming_input/'\n",
    "os.makedirs(stream_dir, exist_ok=True)\n",
    "\n",
    "# Load the full sales data file (assumes it's not too huge for RAM)\n",
    "df = pd.read_csv(sales_file)\n",
    "\n",
    "# Look at the columns so you can pick a split key\n",
    "print(\"Columns:\", df.columns)\n",
    "\n",
    "# Example: Split by date (adjust 'Order Date' if your file has a different name!)\n",
    "split_col = 'YEAR'\n",
    "\n",
    "# Convert to datetime if not already\n",
    "df[split_col] = pd.to_datetime(df[split_col])\n",
    "\n",
    "# Group by just date (not date+time if time exists)\n",
    "df['date_only'] = df[split_col].dt.date\n",
    "\n",
    "# Split by each unique day\n",
    "for date_val, group in df.groupby('date_only'):\n",
    "    out_path = os.path.join(stream_dir, f'sales_{date_val}.csv')\n",
    "    # Drop helper/date_only column for output\n",
    "    group.drop(columns='date_only').to_csv(out_path, index=False)\n",
    "    print(f\"Wrote: {out_path} ({len(group)} records)\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
