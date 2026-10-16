--
-- PostgreSQL database dump
--


-- Dumped from database version 18.4
-- Dumped by pg_dump version 18.4

-- Started on 2026-10-15 13:10:12

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 222 (class 1259 OID 24584)
-- Name: form_responces; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.form_responces (
    form_submission_date timestamp without time zone,
    school_id text NOT NULL,
    school_name text,
    city text,
    state text,
    contact_number text,
    email_id text,
    no_of_students integer
);


--
-- TOC entry 220 (class 1259 OID 16397)
-- Name: performance_input; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.performance_input (
    attempt_id text NOT NULL,
    child_id text,
    school_id text,
    submitted_at timestamp without time zone,
    status text
);


--
-- TOC entry 221 (class 1259 OID 24576)
-- Name: performance_metrics; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.performance_metrics (
    metric_id text NOT NULL,
    input_id text,
    processed_date date,
    wpm double precision,
    wcpm double precision,
    pronunciation double precision,
    fluency double precision,
    noise double precision
);


--
-- TOC entry 219 (class 1259 OID 16389)
-- Name: student_details; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.student_details (
    id text NOT NULL,
    name text,
    contact_number character varying(15),
    email_id text,
    grade text,
    school_id text
);


--
-- TOC entry 4773 (class 2606 OID 24591)
-- Name: form_responces form_responces_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.form_responces
    ADD CONSTRAINT form_responces_pkey PRIMARY KEY (school_id);


--
-- TOC entry 4769 (class 2606 OID 16404)
-- Name: performance_input performance_input_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.performance_input
    ADD CONSTRAINT performance_input_pkey PRIMARY KEY (attempt_id);


--
-- TOC entry 4771 (class 2606 OID 24583)
-- Name: performance_metrics performance_metrics_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.performance_metrics
    ADD CONSTRAINT performance_metrics_pkey PRIMARY KEY (metric_id);


--
-- TOC entry 4767 (class 2606 OID 16396)
-- Name: student_details student_details_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.student_details
    ADD CONSTRAINT student_details_pkey PRIMARY KEY (id);


-- Completed on 2026-10-15 13:10:12

--
-- PostgreSQL database dump complete
--

